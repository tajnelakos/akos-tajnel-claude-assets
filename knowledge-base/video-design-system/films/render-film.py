"""Render a Seekridge film composition (films/*.html) to MP4, or to a contact sheet of stills.

Needs: Python 3.10+, Playwright for Python with a Chromium/Chrome, ffmpeg, Pillow (stills only).

  # check stills first: one frame per time, joined into a contact sheet
  python render-film.py story-fixed-rate-dach-16x9.html --stills 4.5,9.5,15.5,21,30.5,36.5 --out ../assets/Stills/contact-story.jpg

  # full render: one MP4 per scene, joined without re-encoding
  python render-film.py story-fixed-rate-dach-16x9.html --out ../assets/Films/story-fixed-rate-dach-16x9.mp4

Options:
  --fps 30           frame rate (the system's default)
  --crf 18           x264 quality
  --font-css FILE    extra CSS injected before rendering (the fonts are bundled in ../fonts and
                     loaded by ../tokens.css, so this is only needed to override them)
  --chrome PATH      browser executable, if Playwright's bundled one isn't installed

How it works: the page's film engine (components/film-engine.js) draws any time t exactly with
PWV.seek(t). Each scene ([data-scene] with data-start and data-end) is captured frame by frame as
JPEG (quality 92), piped into ffmpeg, written to a temporary name and renamed when ffmpeg exits 0.
The scene files share size, frame rate and encoder settings, so the concat demuxer joins them
with -c copy. Add sound afterwards with: ffmpeg -i film.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac out.mp4
"""
import argparse, asyncio, os, subprocess, sys, tempfile, shutil


async def run(a):
    from playwright.async_api import async_playwright
    page_url = 'file://' + os.path.abspath(a.film)
    extra_css = open(a.font_css).read() if a.font_css else ''
    async with async_playwright() as p:
        kw = {'args': ['--allow-file-access-from-files', '--force-color-profile=srgb']}
        if a.chrome:
            kw['executable_path'] = a.chrome
        b = await p.chromium.launch(**kw)
        pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
        await pg.add_init_script('window.PWV_RENDER = true')
        if a.font_css:
            await pg.route('**/fonts.googleapis.com/**', lambda r: r.abort())
        await pg.goto(page_url)
        await pg.add_style_tag(content=extra_css + 'html,body{background:#000}body{display:block}.frame{transform:none!important}')
        await pg.evaluate('document.fonts.ready')
        await pg.wait_for_timeout(400)
        stage = await pg.query_selector('.pwv-stage')

        async def frame(t):
            await pg.evaluate(f'PWV.seek({t:.5f})')
            return await stage.screenshot(type='jpeg', quality=92)

        if a.stills:
            from PIL import Image
            import io
            times = [float(x) for x in a.stills.split(',')]
            shots = [Image.open(io.BytesIO(await frame(t))) for t in times]
            if a.each:
                os.makedirs(a.each, exist_ok=True)
                for t, im in zip(times, shots):
                    im.save(os.path.join(a.each, f'still-{t:05.2f}.jpg'), quality=90)
            cols = 2 if len(shots) > 1 else 1
            rows = (len(shots) + cols - 1) // cols
            W, H = 960, 540
            sheet = Image.new('RGB', (W * cols + 16 * (cols + 1), H * rows + 16 * (rows + 1)), (233, 232, 226))
            for i, im in enumerate(shots):
                sheet.paste(im.resize((W, H)), (16 + (i % cols) * (W + 16), 16 + (i // cols) * (H + 16)))
            sheet.save(a.out, quality=88)
            print('contact sheet', a.out)
            await b.close()
            return

        scenes = await pg.evaluate("""[...document.querySelectorAll('[data-scene]')]
            .map(s => [parseFloat(s.dataset.start), parseFloat(s.dataset.end)])""")
        work = tempfile.mkdtemp(prefix='pwv-render-')
        parts = []
        for k, (s, e) in enumerate(scenes):
            n = round((e - s) * a.fps)
            tmp = os.path.join(work, f'scene{k:02d}.part.mp4')
            final = os.path.join(work, f'scene{k:02d}.mp4')
            ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(a.fps),
                                   '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', str(a.crf),
                                   '-pix_fmt', 'yuv420p', '-r', str(a.fps), '-an', tmp], stdin=subprocess.PIPE)
            for i in range(n):
                ff.stdin.write(await frame(s + i / a.fps))
            ff.stdin.close()
            if ff.wait() != 0:
                sys.exit(f'ffmpeg failed on scene {k}')
            os.rename(tmp, final)
            parts.append(final)
            print(f'scene {k + 1}/{len(scenes)}: {s:.1f}-{e:.1f}s, {n} frames')
        await b.close()
    lst = os.path.join(work, 'list.txt')
    open(lst, 'w').write(''.join(f"file '{x}'\n" for x in parts))
    tmp_out = a.out[:-4] + '.part.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy',
                    '-movflags', '+faststart', tmp_out], check=True)
    os.replace(tmp_out, a.out)
    shutil.rmtree(work, ignore_errors=True)
    print('wrote', a.out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('film')
    ap.add_argument('--out', required=True)
    ap.add_argument('--stills')
    ap.add_argument('--each', help='with --stills: also save each still as a full-size JPEG in this folder')
    ap.add_argument('--fps', type=int, default=30)
    ap.add_argument('--crf', type=int, default=18)
    ap.add_argument('--font-css')
    ap.add_argument('--chrome')
    asyncio.run(run(ap.parse_args()))
