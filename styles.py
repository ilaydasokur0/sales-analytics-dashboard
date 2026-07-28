import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* En üstteki Deploy / Header barını tamamen gizleme */
header[data-testid="stHeader"] {
    display: none !important;
}

[data-testid="stMainBlockContainer"], .block-container {
    padding-top: 2.5rem !important;
    padding-bottom: 1rem !important;
}

[data-testid="stMainBlockContainer"] [data-testid="stHorizontalBlock"]:first-of-type {
    margin-top: 1.2rem !important;
}
.page-title {
    margin-bottom: 0.3rem !important;
}

.page-title + .stCaption, 
.page-title + p {
    margin-bottom: 0.8rem !important;
} 

html, body, [class*="css"]{
    font-family:"Segoe UI",sans-serif;
}

:root{
    --bg:#F4F9FC;
    --navy:#0A2B47;
    --navy-dark:#041726;
    --accent:#00A8B5;
    --muted:rgba(10,43,71,0.06);
    --card-bg:#FFFFFF;
    --radius:18px;
    --shadow-md:0 18px 40px rgba(4,23,38,0.08);
}

.stApp{
    background:var(--bg);
}

section[data-testid="stSidebar"]{
    background:var(--navy);
    border-right:1px solid rgba(4,23,38,0.6);
}

header,
div[data-testid="stToolbar"],
div[data-testid="stHeader"]{
    background:var(--bg) !important;
    color:var(--navy) !important;
}
.block-container{
    max-width:1800px;
    padding-top:2.4rem;
    padding-bottom:0.35rem;
}

[data-testid="stVerticalBlock"]{
    gap:0.5rem !important;
}

div[data-testid="element-container"],
.element-container{
    margin-bottom:0 !important;
}

/* st.container(border=True) iç boşluğunu daralt */
div[data-testid="stVerticalBlockBorderWrapper"]{
    padding:0.5rem 0.65rem !important;
}

.page-title,
.sidebar-title,
.section-title,
h1,h2,h3{
    color:var(--navy) !important;
}

section[data-testid="stSidebar"] .sidebar-title{
    color:#FFFFFF !important;
}
section[data-testid="stSidebar"] .mini-section-title{
    color:rgba(230,251,250,0.95) !important;
}
.sidebar-title{
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    line-height: 1.2;
}                

section[data-testid="stSidebar"] div[data-baseweb="select"]>div{
    border-color:rgba(255,255,255,0.08) !important;
    background:rgba(255,255,255,0.02) !important;
    color:#FFFFFF !important;
}
section[data-testid="stSidebar"] div[data-baseweb="select"]>div:hover,
section[data-testid="stSidebar"] div[data-baseweb="select"]>div:focus{
    border-color:var(--accent) !important;
    color:var(--accent) !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child{
    border-color:rgba(255,255,255,0.12) !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child div{
    background:#00A8B5 !important;
}
section[data-testid="stSidebar"] .filter-item:hover{color:var(--accent) !important;}
section[data-testid="stSidebar"] .stButton>button,
section[data-testid="stSidebar"] button{
    background:transparent !important;
    border:0.5px solid rgba(255,255,255,0.08) !important;
    color:#FFFFFF !important;
}
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span{
    color:#E6FBFA !important;
}
section[data-testid="stSidebar"] .st-key-month_grid .stButton>button{
    padding:0.2rem 0.3rem !important;
    min-height:1.8rem !important;
    font-size:0.78rem !important;
}
section[data-testid="stSidebar"] .st-key-month_grid button[kind="primary"]{
    background:var(--accent) !important;
    border:0.5px solid var(--accent) !important;
    color:#FFFFFF !important;
    font-weight:700 !important;
}
section[data-testid="stSidebar"] .st-key-month_grid button[kind="primary"]:hover{
    background:var(--accent) !important;
    border-color:var(--accent) !important;
    opacity:0.9;
}

.page-title{
    font-size:1.7rem;
    line-height:1.1;
    font-weight:800;
}

.sidebar-filter-summary{
    font-size:0.78rem;
    color:#E6FBFA;
    font-weight:700;
    margin-top:0.5rem;
    margin-bottom:1.2rem;
}

.page-title + .stCaption + .stCaption {
    margin-top: 0.05rem !important;
    margin-bottom: 0.05rem !important;
}

.section-title{
    font-size:13px;
    font-weight:800;
    margin-bottom:.25rem;
    padding-bottom:.2rem;
    border-bottom:3px solid #DCEFFA;
}

.section-title--large{font-size:15px;}

.mini-section-title{
    font-size:10px;
    font-weight:700;
    text-transform:uppercase;
    color:#6787A5;
    margin-bottom:.2rem;
}

.dashboard-section{
    background:var(--card-bg);
    border:1px solid var(--muted);
    border-radius:var(--radius);
    padding: 16px 20px !important;
    margin-bottom:12px !important;
    box-shadow:var(--shadow-md);
    transition:transform .18s ease, box-shadow .18s ease;
}

.dashboard-section:hover{
    transform:translateY(-6px);
    box-shadow:0 30px 60px rgba(4,23,38,0.12);
}

[data-testid="stHorizontalBlock"] {
    gap: 0.5rem !important;
}

[data-testid="column"] {
    padding: 0 !important;
}

div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #D0DFEE !important;
    border-top: 4px solid #0F2E4F !important;
    border-radius: 8px !important;
    padding: 8px 6px !important;
    height: 70px !important;
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
    font-size: 10.5px !important;
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
    font-size: 17px !important;
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
    font-size: 9.5px !important;
    font-weight: 700 !important;
    margin-top: 2px !important;
    width: 100% !important;
}

div[data-testid="stMetricDelta"] > div[aria-label*="increase"] {
    background-color: #E6F4EA !important;
    color: #137333 !important;
    padding: 1px 6px !important;
    border-radius: 8px !important;
}

div[data-testid="stMetricDelta"] > div[aria-label*="decrease"] {
    background-color: #FCE8E6 !important;
    color: #C5221F !important;
    padding: 1px 6px !important;
    border-radius: 8px !important;
}

.distribution-selected-value{
    display:flex;
    align-items:center;
    justify-content:center;
    min-height:50px;
    font-size:22px;
    font-weight:800;
    color:#245274;
    letter-spacing:0.01em;
}

.product-info-card{
    display:flex;
    flex-direction:column;
    gap:0.25rem;
    padding:0.1rem 0 0;
}

.product-info-row{
    display:grid;
    grid-template-columns:minmax(0, 1fr) auto;
    align-items:center;
    gap:1rem;
    padding:0.18rem 0;
}

.product-info-row + .product-info-row{
    border-top:1px solid rgba(10,43,71,0.08);
}

.product-info-label{
    font-size:0.68rem;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing:0.03em;
    color:#6A88A4;
}

.product-info-value{
    justify-self:end;
    text-align:right;
    font-size:0.88rem;
    font-weight:800;
    color:#245274;
    line-height:1.1;
}

.city-summary-card{
    background:linear-gradient(180deg,#FFFFFF,#F7FBFF);
    border:1px solid #D8E8F5;
    border-left:4px solid #1E3A5F;
    border-radius:16px;
    padding:12px;
    box-shadow:0 8px 20px rgba(83,133,176,.08);
}

.city-summary-stack{
    height:180px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    gap:0.6rem;
}

.city-summary-label{
    font-size:11px;
    text-transform:uppercase;
    color:#6A88A4;
    font-weight:700;
}

.city-summary-value{
    font-size:19px;
    color:#245274;
    font-weight:800;
}

.horizontal-bar-chart{
    display:flex;
    flex-direction:column;
    gap:0.4rem;
    padding-top:0.05rem;
    width:100%;
    max-width:100%;
    justify-content:space-around !important;
}

.horizontal-bar-row{
    display:grid;
    grid-template-columns:minmax(0, 2fr) minmax(56px, 1fr) max-content;
    align-items:center;
    gap:0.4rem;
    padding:0.28rem 0;
    width:100%;
    box-sizing:border-box;
}

.horizontal-bar-name{
    font-size:0.8rem;
    font-weight:800;
    color:#0A2B47;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    min-width:0;
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

.horizontal-bar-meta{
    display:flex;
    flex-direction:column;
    align-items:flex-end;
    gap:0.1rem;
    white-space:nowrap;
    min-width:58px;
}

.horizontal-bar-amount{
    font-size:0.76rem;
    font-weight:800;
    color:#245274;
}

.horizontal-bar-pct{
    justify-self:end;
    text-align:right;
    font-size:0.72rem;
    font-weight:800;
    color:#245274;
    min-width:44px;
    white-space:nowrap;
}

@media (min-width: 1101px){
    .horizontal-bar-row + .horizontal-bar-row{
        margin-top:0.02rem;
    }
}

@media (max-width: 1100px){
    .horizontal-bar-row{
        grid-template-columns:1fr;
        gap:0.3rem;
        padding:0.3rem 0;
    }

    .horizontal-bar-pct{
        justify-self:start;
        text-align:left;
        min-width:0;
    }
}


/* ---------------- GAUGE (YARIM DAİRE) - BÜYÜTME VE TAM ORTALAMA FIX ---------------- */

/* 1. Kapsayıcı Bloğu Kartın İçinde Dikey/Yatay Tam Ortalar */
.gauge-pair {
    display: flex !important;
    align-items: center !important;
    justify-content: space-evenly !important; /* Daireleri kartın geneline eşit dağıtır */
    width: 100% !important;
    height: 100% !important;
    min-height: 140px !important; /* Kartın içini doldurması için yükseklik */
    margin: 0 auto !important;
    padding: 0.5rem 0 !important;
}

.gauge-block {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    flex: 1 !important; /* Her iki gauge eşit alan kaplar */
    min-width: 0 !important;
}

/* 2. Daire Boyutları Büyütüldü (130px Çap) */
.gauge-half-wrap {
    position: relative !important;
    width: 130px !important;
    height: 65px !important;
    overflow: hidden !important;
    margin: 0.4rem auto !important;
}

.gauge-half {
    position: absolute !important;
    left: 0 !important;
    top: 0 !important;
    width: 130px !important;
    height: 130px !important;
    border-radius: 50% !important;
}

/* 3. İç Delik ve Yüzde Değeri Boyutları */
.gauge-hole {
    position: absolute !important;
    left: 50% !important;
    bottom: 0 !important;
    width: 72px !important;
    height: 72px !important;
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
    font-size: 16px !important;
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
    margin-top: 0.4rem !important;
    flex-wrap: nowrap !important;
}

.gauge-legend-item {
    display: flex !important;
    align-items: center !important;
    gap: 0.2rem !important;
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    white-space: nowrap !important;
}

/* ---------------- DONUT CHART TAM ORTALAMA FIX ---------------- */

/* Kartın içindeki Donut kapsayıcısını dikey ve yatayda tam ortalar */
.donut-chart {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;     /* Dikeyde tam ortalama */
    justify-content: center !important;  /* Yatayda tam ortalama */
    gap: 1.2rem !important;
    width: 100% !important;
    height: 100% !important;
    min-height: 140px !important;       /* Gauge kartıyla aynı yüksekliği yakalar */
    padding: 0.5rem 0 !important;
}

/* Donut halkasını dikey hizada sabit tutma */
.donut-chart-circle {
    width: 125px !important;
    height: 125px !important;
    border-radius: 50% !important;
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    margin: auto 0 !important;
}

.donut-chart-center {
    width: 70px !important;
    height: 70px !important;
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
    justify-content: flex-start !important; /* Kesilmeyi önlemek için üste hizalar */
    gap: 0.35rem !important;
    height: 100% !important;
    max-height: 150px !important;            /* Yüksekliği esneterek scroll ihtiyacını azaltır */
    overflow-y: auto !important;
    padding-top: 0.2rem !important;          /* Üstten nefes alma boşluğu */
    padding-right: 0.4rem !important;
}

/* Her bir satırın dikey sıkışmasını önleme */
.donut-chart-row {
    display: flex !important;
    align-items: center !important;
    gap: 0.45rem !important;
    padding: 1px 0 !important;
}

.donut-chart-color{
    width:12px;
    height:12px;
    border-radius:50%;
    margin-top:.2rem;
    flex-shrink:0;
}

.donut-chart-text{
    display:flex;
    flex-direction:column;
    min-width:0;
}

.donut-chart-label{
    font-size:.92rem;
    font-weight:700;
    color:#0A2B47;

    overflow:hidden;
    white-space:nowrap;
    text-overflow:ellipsis;
}

.donut-chart-value{
    font-size:.78rem;
    font-weight:700;
    color:#245274;
    white-space:nowrap;
}

div[data-testid="stDataFrame"]{
    border:1px solid #DCE8F3;
    border-radius:14px;
    overflow:hidden;
    box-shadow:0 4px 12px rgba(83,133,176,.05);
}

thead tr th{
    background:#EAF5FD !important;
    color:var(--navy) !important;
    font-weight:800 !important;
}

tbody tr:nth-child(even){
    background:#FAFDFF;
}

div[data-baseweb="select"]>div{
    border:1px solid #D2E4F3 !important;
    border-radius:10px;
}

div[data-baseweb="select"]>div:hover{
    border-color:#7DBAE9 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child{
    border-color:#7DBAE9 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child div{
    background:#7DBAE9 !important;
}

hr{
    border-top:1px solid var(--muted);
    margin:0.6rem 0;
}

header,
div[data-testid="stToolbar"],
div[data-testid="stHeader"]{
    background:#F4F9FC !important;
    color:#0A2B47 !important;
}

.block-container{
    background:linear-gradient(180deg,#F8FBFF,#F4F9FC);
}

.dashboard-section{position:relative;}
.dashboard-section::before{
    content:'';
    position:absolute;
    left:0;
    top:0;
    bottom:0;
    width:6px;
    background:var(--navy);
    border-top-left-radius:var(--radius);
    border-bottom-left-radius:var(--radius);
}

section[data-testid="stSidebar"] div[data-baseweb="select"]>div:focus,
section[data-testid="stSidebar"] .filter-item:focus,
section[data-testid="stSidebar"] .stButton>button:focus{
    outline:3px solid rgba(0,168,181,0.18);
    outline-offset:2px;
}

.transition-smooth{transition:all .18s cubic-bezier(.2,.8,.2,1);}

</style>
""",
        unsafe_allow_html=True,
    )