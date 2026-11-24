# Product UI

The eight Seekridge web-app screens every film panel is rebuilt from (November 2026, demo workspace *Alpenkreis Bank*, 40,000 customers). Names, columns, signal names, layer labels and status badges in films must match these. All figures are demo data. See section 11 of the film book for what each screen gives a film.

| File | Screen | Film use |
|---|---|---|
| `01-signals-this-week.png` | Ranked signals for the week, with top layer and top reason | Signal beat, FocusMarks on one row, scale beat |
| `02-signal-detail.png` | One signal: evidence trail with weights summing to 100, the customer, the suggested action | SignalCard, EvidenceTrail |
| `03-customer-record.png` | The three layers for one customer, side by side, with each source's freshness | LayerStack |
| `04-coverage-map.png` | Postcode areas as lots, filled where signals cluster, one selected in gold | ParcelField, Statements |
| `05-crm-sync.png` | Sync runs to CRM queues, with the one that needs attention | Action beat |
| `06-audit-log.png` | Append-only record of every event on a signal | AuditLog |
| `07-backtest-report.png` | Signal-rank deciles against the book average, with period and n | FigureCard, BacktestChart |
| `08-data-layers.png` | Connected customer, property and market sources and their freshness | Walkthrough openers, governance beats |

The screens are drawn at web density (15px body). On film, panels double it (26px values, 72px rows) and keep only the rows a beat needs.
