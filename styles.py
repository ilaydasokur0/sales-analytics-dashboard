import streamlit as st

def load_css():
    st.markdown("""
<style>

html, body, [class*="css"]{
    font-family:"Segoe UI",sans-serif;
}

.stApp{
    background:#F4F9FC; 
}

section[data-testid="stSidebar"]{
    background:#FBFDFF;
    border-right:1px solid #DCE8F3;
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
    color:#2F5F85 !important;
}

.page-title{
    font-size:38px;
    font-weight:800;
}

.section-title{
    font-size:20px;
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
    background:linear-gradient(180deg,#FFFFFF,#F8FCFF);
    border:1px solid #DCE8F3;
    border-radius:20px;
    padding:24px;
    margin-bottom:28px;
    box-shadow:0 10px 24px rgba(83,133,176,.08);
}

div[data-testid="stMetric"]{
    background:linear-gradient(180deg,#FFFFFF,#F7FBFF);
    border:1px solid #D8E8F5;
    border-left:4px solid #1E3A5F;
    border-radius:16px;
    padding:12px;
    height:96px;
    box-shadow:0 8px 20px rgba(83,133,176,.08);
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
    font-size:24px !important;
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
    color:#2F5F85 !important;
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
    border-top:1px solid #DCE8F3;
    margin:1.6rem 0;
}

</style>
""", unsafe_allow_html=True)
