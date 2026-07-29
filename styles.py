import streamlit as st


def load_css():
    st.markdown(
        """
<style>
/* ---------------- 1. TİPOGRAFİ VE ROOT DEĞİŞKENLERİ ---------------- */
:root {
    --bg: #F4F9FC;
    --navy: #0A2B47;
    --navy-dark: #041726;
    --accent: #00A8B5;
    --muted: rgba(10, 43, 71, 0.06);
    --card-bg: #FFFFFF;
    --radius: 18px;
    --shadow-md: 0 18px 40px rgba(4, 23, 38, 0.08);
}

html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

.stApp {
    background: var(--bg);
}

/* ---------------- 2. LAYOUT & CONTAINER OPTİMİZASYONU ---------------- */
header[data-testid="stHeader"],
div[data-testid="stToolbar"] {
    display: none !important;
    background: var(--bg) !important;
    color: var(--navy) !important;
}

/* Ana konteynır: Üst boşluk optimize edildi ve tekrarlayan selector'lar birleştirildi */
[data-testid="stMainBlockContainer"], 
.block-container {
    max-width: 1880px;
    padding-top: 1.2rem !important;
    padding-bottom: 0.5rem !important;
    background: linear-gradient(180deg, #F8FBFF, #F4F9FC);
}

/* Sayfa başlığı ve alt metin boşlukları */
.page-title {
    font-size: 2.15rem;
    line-height: 1.1;
    font-weight: 800;
    color: var(--navy) !important;
    margin-bottom: 0.25rem !important;
}

.page-title + .stCaption, 
.page-title + p {
    margin-bottom: 0.4rem !important;
}

.page-title + .stCaption + .stCaption {
    margin-top: 0.05rem !important;
    margin-bottom: 0.25rem !important;
}

/* Dikey Spacing Yönetimi */
[data-testid="stVerticalBlock"] {
    gap: 0.75rem !important;
}

[data-testid="stHorizontalBlock"] {
    gap: 0.5rem !important;
}

[data-testid="column"] {
    padding: 0 !important;
}

/* Streamlit Kart Kenarlıkları ve Boşluk Düzenlemeleri */
div[data-testid="stVerticalBlockBorderWrapper"] {
    box-sizing: border-box !important;
    height: 100% !important;
    padding: 6px 10px !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] > div {
    box-sizing: border-box !important;
    padding: 0 !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlock"] {
    height: 100% !important;
    gap: 0.25rem !important;
}

/* ---------------- 3. KOMPAKT KPI & METRİK KARTLARI ---------------- */
.st-key-kpi_section [data-testid="stHorizontalBlock"] {
    gap: 0.4rem !important;
}

div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #D0DFEE !important;
    border-top: 4px solid #0F2E4F !important;
    border-radius: 8px !important;
    padding: 6px 4px !important;
    height: 80px !important;
    box-shadow: 0 4px 12px rgba(15, 46, 79, 0.05) !important;

    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    min-width: 0 !important;
    width: 100% !important;
}

div[data-testid="stMetric"]:hover {
    border-top: 4px solid #0F2E4F !important;
    box-shadow: 0 4px 12px rgba(15, 46, 79, 0.05) !important;
}

div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] > div,
div[data-testid="stMetricLabel"] p {
    font-size: 11.5px !important;
    font-weight: 700 !important;
    color: #4A6E8D !important;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
}

div[data-testid="stMetricLabel"] {
    white-space: normal !important;
    line-height: 1.1 !important;
    max-height: 2.0em !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-bottom: 2px !important;
}

div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] > div,
div[data-testid="stMetricValue"] span {
    font-size: 20px !important;
    font-weight: 800 !important;
    color: #0F2E4F !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    white-space: nowrap !important;
    line-height: 1 !important;
    width: 100% !important;
    margin: 0 auto !important;
}

div[data-testid="stMetricDelta"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    font-size: 9px !important;
    font-weight: 700 !important;
    margin-top: 2px !important;
    width: 100% !important;
}

div[data-testid="stMetricDelta"] > div[aria-label*="increase"] {
    background-color: #E6F4EA !important;
    color: #137333 !important;
    padding: 1px 5px !important;
    border-radius: 6px !important;
}

div[data-testid="stMetricDelta"] > div[aria-label*="decrease"] {
    background-color: #FCE8E6 !important;
    color: #C5221F !important;
    padding: 1px 5px !important;
    border-radius: 6px !important;
}

/* ---------------- 4. SİDEBAR BİLEŞENLERİ ---------------- */
section[data-testid="stSidebar"] {
    background: var(--navy);
    border-right: 1px solid rgba(4, 23, 38, 0.6);
}

.sidebar-title {
    font-size: 1.65rem;
    font-weight: 800;
    margin-bottom: 0.25rem;
    line-height: 1.2;
    color: #FFFFFF !important;
}

.sidebar-comparison-status {
    font-size: 0.72rem;
    line-height: 1.35;
    color: #CBEFF0;
    font-weight: 700;
    margin: 0 0 0.75rem;
}

.sidebar-filter-heading {
    margin: 0.85rem 0 0.35rem;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(255, 255, 255, 0.14);
    color: #E6FBFA;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.sidebar-filter-summary {
    font-size: 0.78rem;
    color: #E6FBFA;
    font-weight: 700;
    margin-top: 0.5rem;
    margin-bottom: 1.2rem;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    border-color: rgba(255, 255, 255, 0.08) !important;
    background: rgba(255, 255, 255, 0.02) !important;
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover,
section[data-testid="stSidebar"] div[data-baseweb="select"] > div:focus {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child {
    border-color: rgba(255, 255, 255, 0.12) !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child div {
    background: #00A8B5 !important;
}

section[data-testid="stSidebar"] .filter-item:hover {
    color: var(--accent) !important;
}

section[data-testid="stSidebar"] .stButton > button,
section[data-testid="stSidebar"] button {
    background: transparent !important;
    border: 0.5px solid rgba(255, 255, 255, 0.08) !important;
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #E6FBFA !important;
}

section[data-testid="stSidebar"] .st-key-month_grid .stButton > button {
    padding: 0.2rem 0.3rem !important;
    min-height: 1.8rem !important;
    font-size: 0.78rem !important;
}

section[data-testid="stSidebar"] .st-key-month_grid button[kind="primary"] {
    background: var(--accent) !important;
    border: 0.5px solid var(--accent) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

section[data-testid="stSidebar"] .st-key-month_grid button[kind="primary"]:hover {
    background: var(--accent) !important;
    border-color: var(--accent) !important;
    opacity: 0.9;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div:focus,
section[data-testid="stSidebar"] .filter-item:focus,
section[data-testid="stSidebar"] .stButton > button:focus {
    outline: 3px solid rgba(0, 168, 181, 0.18);
    outline-offset: 2px;
}

/* ---------------- 5. DÖKÜMAN BÖLÜMLERİ VE GENEL KARTLAR ---------------- */
.section-title {
    box-sizing: border-box;
    min-height: 27px;
    font-size: 15px;
    line-height: 18px;
    font-weight: 800;
    color: var(--navy) !important;
    margin: 0 0 10px;
    padding: 0 0 6px;
    border-bottom: 3px solid #DCEFFA;
}

.section-title--large {
    font-size: 15px;
}

.mini-section-title {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    color: #6787A5;
    margin-bottom: .2rem;
}

section[data-testid="stSidebar"] .mini-section-title {
    color: rgba(230, 251, 250, 0.95) !important;
}

.dashboard-section {
    position: relative;
    background: var(--card-bg);
    border: 1px solid var(--muted);
    border-radius: var(--radius);
    padding: 16px 20px !important;
    margin-bottom: 10px !important;
    box-shadow: var(--shadow-md);
    transition: transform .18s ease, box-shadow .18s ease;
}

.dashboard-section::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 6px;
    background: var(--navy);
    border-top-left-radius: var(--radius);
    border-bottom-left-radius: var(--radius);
}

.dashboard-section:hover {
    transform: translateY(-4px);
    box-shadow: 0 24px 48px rgba(4, 23, 38, 0.10);
}

/* Radio Button Özelleştirmeleri */
div[data-testid="stRadio"] label p {
    font-size: 0.75rem !important;
    font-weight: 700 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {
    width: 11px !important;
    height: 11px !important;
    border-color: #7DBAE9 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child div {
    background: #7DBAE9 !important;
}

div[data-testid="stRadio"] > div {
    gap: 0.6rem !important;
    margin-top: -0.1rem !important;
    margin-bottom: 0.25rem !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stRadio"] {
    margin-bottom: 0.1rem !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stRadio"] > div {
    gap: 0.7rem !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stRadio"] label {
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    color: #245274 !important;
    gap: 0.25rem !important;
    padding: 0 !important;
}

/* ---------------- 6. ÖZEL BİLEŞENLER (GAUGE, DONUT, BAR, RANK) ---------------- */
/* Gauge Bileşeni */
.gauge-pair {
    display: flex !important;
    align-items: center !important;
    justify-content: space-evenly !important;
    width: 100% !important;
    height: 100% !important;
    flex: 1 !important;
    min-height: 0 !important;
    margin: 0 auto !important;
    padding: 0 !important;
}

.gauge-block {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    flex: 1 !important;
    min-width: 0 !important;
}

.gauge-half-wrap {
    position: relative !important;
    width: 164px !important;
    height: 82px !important;
    overflow: hidden !important;
    margin: 0.15rem auto 0 auto !important;
}

.gauge-half {
    position: absolute !important;
    left: 0 !important;
    top: 0 !important;
    width: 164px !important;
    height: 164px !important;
    border-radius: 50% !important;
}

.gauge-hole {
    position: absolute !important;
    left: 50% !important;
    bottom: 0 !important;
    width: 90px !important;
    height: 90px !important;
    border-radius: 50% !important;
    background: #ffffff !important;
    transform: translate(-50%, 50%) !important;
    z-index: 1 !important;
    box-shadow: 0 -2px 6px rgba(0, 0, 0, 0.05) !important;
}

.gauge-center-value {
    position: absolute !important;
    left: 50% !important;
    bottom: 4px !important;
    transform: translateX(-50%) !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    color: #245274 !important;
    line-height: 1 !important;
    z-index: 2 !important;
}

.gauge-legend-row {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 0.6rem !important;
    margin-top: 0.15rem !important;
    flex-wrap: nowrap !important;
}

.gauge-legend-item {
    display: flex !important;
    align-items: center !important;
    gap: 0.2rem !important;
    font-size: 0.76rem !important;
    font-weight: 700 !important;
    white-space: nowrap !important;
}

/* Donut Chart Bileşeni */
.donut-chart {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 0.75rem !important;
    width: 100% !important;
    height: 132px !important;
    flex: 1 !important;
    min-height: 0 !important;
    padding: 0 !important;
}

.donut-chart-circle {
    width: 130px !important;
    height: 130px !important;
    border-radius: 50% !important;
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    margin: auto 0 !important;
}

.donut-chart-circle svg {
    width: 100% !important;
    height: 100% !important;
}

.donut-chart-center {
    width: 72px !important;
    height: 72px !important;
    border-radius: 50% !important;
    background: #FFFFFF !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 2px 8px rgba(0,0,0,.08) !important;
}

.donut-chart-legend {
    flex: 1 !important;
    min-width: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    gap: 0.32rem !important;
    align-self: stretch !important;
    height: 100% !important;
    max-height: 100% !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    box-sizing: border-box !important;
    padding-top: 6px !important;
    padding-right: 0.2rem !important;
}

.donut-chart-row {
    display: grid !important;
    grid-template-columns: 12px minmax(0, 1fr) !important;
    align-items: start !important;
    gap: 0.5rem !important;
    min-height: 28px !important;
    padding: 0 !important;
}

.donut-chart-color {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-top: .15rem;
    flex-shrink: 0;
}

.donut-chart-text {
    display: flex;
    flex-direction: column;
    min-width: 0;
    justify-content: center;
}

.donut-chart-label {
    font-size: .84rem;
    font-weight: 700;
    color: #0A2B47;
    overflow: visible;
    white-space: normal;
    overflow-wrap: anywhere;
    line-height: 1.1;
}

.donut-chart-value {
    font-size: .76rem;
    font-weight: 700;
    color: #245274;
    white-space: nowrap;
    line-height: 1.1;
}

div[data-testid="stVerticalBlockBorderWrapper"]:has(.gauge-pair) [data-testid="stVerticalBlock"],
div[data-testid="stVerticalBlockBorderWrapper"]:has(.donut-chart) [data-testid="stVerticalBlock"] {
    display: flex !important;
    flex-direction: column !important;
    height: 100% !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:has(.gauge-pair) [data-testid="stElementContainer"]:has(.gauge-pair),
div[data-testid="stVerticalBlockBorderWrapper"]:has(.donut-chart) [data-testid="stElementContainer"]:has(.donut-chart) {
    display: flex !important;
    flex: 1 !important;
    min-height: 0 !important;
}

/* Horizontal Bar Chart */
.horizontal-bar-chart {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
    padding: 0;
    width: 100%;
    max-width: 100%;
    justify-content: flex-start !important;
}

.horizontal-bar-row {
    display: grid;
    grid-template-columns: minmax(0, 2fr) minmax(56px, 1fr) max-content;
    align-items: center;
    gap: 0.4rem;
    padding: 0.2rem 0;
    width: 100%;
    box-sizing: border-box;
}

.horizontal-bar-name {
    font-size: 0.8rem;
    font-weight: 800;
    color: #0A2B47;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    min-width: 0;
}

.horizontal-bar-track {
    width: 100%;
    height: 7px;
    background: #E5EEF5;
    border-radius: 999px;
    overflow: hidden;
}

.horizontal-bar-bar {
    height: 9px;
    background: navy;
}

.horizontal-bar-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.1rem;
    white-space: nowrap;
    min-width: 58px;
}

.horizontal-bar-amount {
    font-size: 0.76rem;
    font-weight: 800;
    color: #245274;
}

.horizontal-bar-pct {
    justify-self: end;
    text-align: right;
    font-size: 0.72rem;
    font-weight: 800;
    color: #245274;
    min-width: 44px;
    white-space: nowrap;
}

/* City Rank Card - (3 kez tekrarlanan tanım teke düşürüldü) */
.city-rank-card {
    background: linear-gradient(180deg, #F8FCFF 0%, #EEF7FF 100%);
    border: 1px solid #D9E9F6;
    border-radius: 16px;
    padding: 18px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-shadow: 0 4px 12px rgba(18, 67, 104, .06);
}

.city-rank-title {
    font-size: .92rem;
    font-weight: 700;
    color: #4A6782;
    margin-bottom: 18px;
}

.city-rank-number {
    font-size: 2.9rem;
    font-weight: 900;
    color: #173B57;
    line-height: 1;
    margin-bottom: 22px;
}

.city-rank-number span {
    font-size: 1.15rem;
    color: #93A6B7;
    font-weight: 600;
}

.city-rank-benchmark {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    font-size: .95rem;
    font-weight: 800;
    white-space: nowrap;
}

.benchmark-up { color: #16A34A; }
.benchmark-down { color: #DC2626; }
.benchmark-icon { font-size: 1rem; font-weight: 900; }

/* Dynamic Info Cards */
.distribution-selected-value {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 50px;
    font-size: 22px;
    font-weight: 800;
    color: #245274;
    letter-spacing: 0.01em;
}

.product-info-card {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    padding: 0.1rem 0 0;
}

.product-info-row {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    align-items: center;
    gap: 1rem;
    padding: 0.18rem 0;
}

.product-info-row + .product-info-row {
    border-top: 1px solid rgba(10, 43, 71, 0.08);
}

.product-info-label {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    color: #6A88A4;
}

.product-info-value {
    justify-self: end;
    text-align: right;
    font-size: 0.88rem;
    font-weight: 800;
    color: #245274;
    line-height: 1.1;
}

.city-summary-card {
    background: linear-gradient(180deg, #FFFFFF, #F7FBFF);
    border: 1px solid #D8E8F5;
    border-left: 4px solid #1E3A5F;
    border-radius: 16px;
    padding: 12px;
    box-shadow: 0 8px 20px rgba(83, 133, 176, .08);
}

.city-summary-stack {
    height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.6rem;
}

.city-summary-label {
    font-size: 11px;
    text-transform: uppercase;
    color: #6A88A4;
    font-weight: 700;
}

.city-summary-value {
    font-size: 19px;
    color: #245274;
    font-weight: 800;
}

/* ---------------- 7. DİĞER BİLEŞENLER VE MEDIA QUERIES ---------------- */
div[data-testid="stDataFrame"] {
    border: 1px solid #DCE8F3;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(83, 133, 176, .05);
}

thead tr th {
    background: #EAF5FD !important;
    color: var(--navy) !important;
    font-weight: 800 !important;
}

tbody tr:nth-child(even) {
    background: #FAFDFF;
}

div[data-baseweb="select"] > div {
    border: 1px solid #D2E4F3 !important;
    border-radius: 10px;
}

div[data-baseweb="select"] > div:hover {
    border-color: #7DBAE9 !important;
}

hr {
    border-top: 1px solid var(--muted);
    margin: 0.6rem 0;
}

.transition-smooth {
    transition: all .18s cubic-bezier(.2, .8, .2, 1);
}

@media (min-width: 1101px) {
    .horizontal-bar-row + .horizontal-bar-row {
        margin-top: 0.02rem;
    }
}

@media (max-width: 1100px) {
    .horizontal-bar-row {
        grid-template-columns: 1fr;
        gap: 0.3rem;
        padding: 0.3rem 0;
    }

    .horizontal-bar-pct {
        justify-self: start;
        text-align: left;
        min-width: 0;
    }
}
</style>
""",
        unsafe_allow_html=True,
    )