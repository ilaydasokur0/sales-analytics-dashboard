import streamlit as st

def load_css():
    st.markdown("""
<style>

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

/* Sidebar: slightly darker than page */
section[data-testid="stSidebar"]{
    background:var(--navy);
    border-right:1px solid rgba(4,23,38,0.6);
}

/* Top header / deploy ribbon: lighter (page background) */
header,
div[data-testid="stToolbar"],
div[data-testid="stHeader"]{
    background:var(--bg) !important;
    color:var(--navy) !important;
}

.block-container{
    max-width:1800px;
    padding-top:2.6rem;
    padding-bottom:2rem;
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
    font-size: 1.8rem;
    font-weight: 800;
    margin-bottom: 1rem;
    line-height: 1.2;
}                
/* Sidebar scoped inputs and controls */
/* Sidebar controls: accent on hover/focus */
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
    border:1px solid rgba(255,255,255,0.08) !important;
    color:#FFFFFF !important;
}
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span{
    color:#E6FBFA !important;
}

/* Ay seçim grid'i: kompakt kutular, seçili ay filtre kaldırılana kadar mavi kalır */
section[data-testid="stSidebar"] .st-key-month_grid .stButton>button{
    padding:0.2rem 0.3rem !important;
    min-height:1.8rem !important;
    font-size:0.78rem !important;
}
section[data-testid="stSidebar"] .st-key-month_grid button[kind="primary"]{
    background:var(--accent) !important;
    border:1px solid var(--accent) !important;
    color:#FFFFFF !important;
    font-weight:700 !important;
}
section[data-testid="stSidebar"] .st-key-month_grid button[kind="primary"]:hover{
    background:var(--accent) !important;
    border-color:var(--accent) !important;
    opacity:0.9;
}

.page-title{
    font-size:3.2rem;
    line-height:1.02;
    font-weight:800;
}

/* Reduce vertical gap between two consecutive captions that follow the page title
   (keeps spacing between page title and first caption unchanged) */
.page-title + .stCaption + .stCaption {
    margin-top: 0.15rem !important;
    margin-bottom: 0.15rem !important;
}

.section-title{
    font-size:18px;
    font-weight:800;
    margin-bottom:.5rem;
    padding-bottom:.45rem;
    border-bottom:3px solid #DCEFFA;
}

.section-title--large{font-size:19px;}

.mini-section-title{
    font-size:12px;
    font-weight:700;
    text-transform:uppercase;
    color:#6787A5;
}

.dashboard-section{
    background:var(--card-bg);
    border:1px solid var(--muted);
    border-radius:var(--radius);
    padding:24px;
    margin-bottom:28px;
    box-shadow:var(--shadow-md);
    transition:transform .18s ease, box-shadow .18s ease;
}

.dashboard-section:hover{
    transform:translateY(-6px);
    box-shadow:0 30px 60px rgba(4,23,38,0.12);
}

div[data-testid="stMetric"]{
    background:linear-gradient(180deg,#FFFFFF,#F7FBFF);
    border:1px solid var(--muted);
    border-left:4px solid var(--navy);
    border-radius:16px;
    padding:12px;
    height:110px;
    box-shadow:0 8px 20px rgba(4,23,38,0.06);
}

div[data-testid="stMetricLabel"]{
    font-size:12px !important;
    font-weight:700 !important;
    color:#6A88A4 !important;
    text-transform:uppercase;
}

div[data-testid="stMetricValue"]{
    font-size:26px !important;
    font-weight:800 !important;
    color:#245274 !important;
}

.distribution-selected-value{
    display:flex;
    align-items:center;
    justify-content:center;
    min-height:64px;
    font-size:26px;
    font-weight:800;
    color:#245274;
    letter-spacing:0.01em;
}

.product-info-card{
    display:flex;
    flex-direction:column;
    gap:0.4rem;
    padding:0.15rem 0 0;
    min-height:210px;
}

.product-info-row{
    display:grid;
    grid-template-columns:minmax(0, 1fr) auto;
    align-items:center;
    gap:1rem;
    padding:0.28rem 0;
}

.product-info-row + .product-info-row{
    border-top:1px solid rgba(10,43,71,0.08);
}

.product-info-label{
    font-size:0.74rem;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing:0.03em;
    color:#6A88A4;
}

.product-info-value{
    justify-self:end;
    text-align:right;
    font-size:0.98rem;
    font-weight:800;
    color:#245274;
    line-height:1.15;
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
    height:248px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    gap:0.95rem;
}

.city-summary-label{
    font-size:11px;
    text-transform:uppercase;
    color:#6A88A4;
    font-weight:700;
}

.city-summary-value{
    font-size:22px;
    color:#245274;
    font-weight:800;
}

.horizontal-bar-chart{
    display:flex;
    flex-direction:column;
    gap:1rem;
    padding-top:0.15rem;
    width:100%;
    max-width:100%;
}

.horizontal-bar-row{
    display:grid;
    grid-template-columns:minmax(0, 2fr) minmax(72px, 1fr) max-content;
    align-items:center;
    gap:0.55rem;
    padding:0.7rem 0;
    width:100%;
    box-sizing:border-box;
}

.horizontal-bar-name{
    font-size:0.94rem;
    font-weight:800;
    color:#0A2B47;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    min-width:0;
}

.horizontal-bar-track {
    width: 100%;
    height: 10px;
    background: #E5EEF5;
    border-radius: 999px;
    overflow: hidden;
}

.horizontal-bar-bar {
    height: 12px;
    background: navy;
}

.horizontal-bar-meta{
    display:flex;
    flex-direction:column;
    align-items:flex-end;
    gap:0.1rem;
    white-space:nowrap;
    min-width:76px;
}

.horizontal-bar-amount{
    font-size:0.9rem;
    font-weight:800;
    color:#245274;
}

.horizontal-bar-pct{
    justify-self:end;
    text-align:right;
    font-size:0.84rem;
    font-weight:800;
    color:#245274;
    min-width:56px;
    white-space:nowrap;
}

@media (min-width: 1101px){
    .horizontal-bar-row + .horizontal-bar-row{
        margin-top:0.05rem;
    }
}

@media (max-width: 1100px){
    .horizontal-bar-row{
        grid-template-columns:1fr;
        gap:0.45rem;
        padding:0.65rem 0;
    }

    .horizontal-bar-pct{
        justify-self:start;
        text-align:left;
        min-width:0;
    }
}

.donut-chart{
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:1.75rem;
    width:100%;
}

.donut-chart-circle{
    width:220px;
    height:220px;
    border-radius:50%;
    position:relative;

    display:flex;
    align-items:center;
    justify-content:center;

    flex-shrink:0;
}

.donut-chart-center{
    width:130px;
    height:130px;
    border-radius:50%;
    background:#FFFFFF;

    display:flex;
    align-items:center;
    justify-content:center;

    box-shadow:0 2px 8px rgba(0,0,0,.08);
}

.donut-chart-legend{
    width:100%;
    display:flex;
    flex-direction:column;
    gap:.75rem;
}

.donut-chart-row{
    display:grid;
    grid-template-columns:18px 1fr auto;
    align-items:center;
    gap:.75rem;
}

.donut-chart-color{
    width:12px;
    height:12px;
    border-radius:50%;
}

.donut-chart-label{
    font-size:.95rem;
    font-weight:700;
    color:#0A2B47;

    overflow:hidden;
    white-space:nowrap;
    text-overflow:ellipsis;
}

.donut-chart-value{
    font-size:.9rem;
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
    margin:1.6rem 0;
}

/* Top header / deploy ribbon: match page background (lighter) */
header,
div[data-testid="stToolbar"],
div[data-testid="stHeader"]{
    background:#F4F9FC !important;
    color:#0A2B47 !important;
}

/* Subtle page container tone */
.block-container{
    background:linear-gradient(180deg,#F8FBFF,#F4F9FC);
}

/* Left accent stripe on dashboard sections to match sidebar */
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

/* Accessibility: focus outlines for sidebar controls */
section[data-testid="stSidebar"] div[data-baseweb="select"]>div:focus,
section[data-testid="stSidebar"] .filter-item:focus,
section[data-testid="stSidebar"] .stButton>button:focus{
    outline:3px solid rgba(0,168,181,0.18);
    outline-offset:2px;
}

/* Smooth transitions helper */
.transition-smooth{transition:all .18s cubic-bezier(.2,.8,.2,1);}

</style>
""", unsafe_allow_html=True)