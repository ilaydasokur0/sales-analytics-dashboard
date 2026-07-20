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

.page-title{
    font-size:40px;
    line-height:1.02;
    font-weight:800;
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
    height:96px;
    box-shadow:0 8px 20px rgba(4,23,38,0.06);
    transition:all .2s ease;
}

div[data-testid="stMetric"]:hover{
    transform:translateY(-4px);
    background:#F2FAFF;
    border-color:#A9D4F5;
    box-shadow:0 14px 30px rgba(83,133,176,.16);
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
