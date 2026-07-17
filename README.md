# Sales Dashboard

Project purpose:
- Interactive Streamlit dashboard for analyzing sales data from sample CSV files.

Technologies:
- Python 3.10+
- Streamlit
- pandas
- numpy

Project structure:
- `app.py` - Streamlit app entrypoint
- `analysis.py` - data loading and transformation helpers
- `styles.py` - css loader for Streamlit
- `components/` - UI components (sidebar, KPI, charts, overview, city, customer)
- `utils/` - utility helpers (formatting, table builders, metrics)
- `data/` - example CSV data files

Setup
1. Create and activate a Python virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

Dashboard features
- Date, city, customer and product filters in sidebar
- KPIs with period-over-period deltas
- Monthly line charts and distribution (PL / product type)
- Ranked tables for top/bottom customers, cities and products

Notes
- This repository is structured for clarity and reuse: UI components live under `components/` and smaller helpers under `utils/`.
- No behavior has been changed from the original implementation; this README documents the existing app.
