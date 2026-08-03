import streamlit as st


def load_css():
    st.markdown(
        """
<style>
:root {
    --bg: #E7EEF6;
    --navy: #0A2B47;
    --navy-dark: #041726;
    --accent: #00A8B5;
    --muted: rgba(10, 43, 71, 0.06);
    --card-bg: #FFFFFF;
    --radius: 18px;
    --shadow-md: 0 18px 40px rgba(4, 23, 38, 0.08);
}

html, body, [class*="css"] {
    font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: var(--bg);
}

header[data-testid="stHeader"] {
    display: none !important;
}

div[data-testid="stToolbar"],
div[data-testid="stDecoration"] {
    display: none !important;
}

.st-key-sidebar_toggle_wrap {
    position: fixed !important;
    top: 12px !important;
    left: 12px !important;
    z-index: 999999 !important;
}

.st-key-sidebar_toggle_wrap .stButton > button {
    width: 34px !important;
    height: 34px !important;
    min-width: 34px !important;
    padding: 0 !important;
    background: #0A2B47 !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 8px !important;
    color: #FFFFFF !important;
    font-size: 1.05rem !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
}

.st-key-sidebar_toggle_wrap .stButton > button:hover {
    background: #00A8B5 !important;
}

[data-testid="stMainBlockContainer"], 
.block-container {
    max-width: 1880px;
    padding-top: 0.35rem !important;  
    padding-bottom: 0.2rem !important;
    background: linear-gradient(180deg, #EEF3F9 0%, #E7EEF6 100%);
}

.header-title-container {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;         
    margin-top: 0 !important;
    margin-bottom: 0.6rem !important; 
    padding-left: 0 !important;       
    margin-left: 0 !important;
    width: 100% !important;
    position: relative !important;
    z-index: 999 !important;
}

.header-icon-box {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 30px !important;        
    height: 30px !important;
    flex-shrink: 0 !important;
    position: relative !important;
}

.header-icon-box svg {
    width: 28px !important;           
    height: 28px !important;
    min-width: 28px !important;
    min-height: 28px !important;
    max-width: 28px !important;
    max-height: 28px !important;
    display: block !important;
}

.header-icon-box::after {
    content: '' !important;
    display: block !important;
    position: absolute !important;
    right: -7px !important;             
    top: 50% !important;
    transform: translateY(-50%) !important;
    width: 2px !important;           
    height: 20px !important;            
    background: #00A8B5 !important;   
    border-radius: 2px !important;
}

.gradient-page-title,
.page-title {
    font-size: 1.95rem !important;
    line-height: 1.1 !important;
    font-weight: 800 !important;
    color: var(--navy, #0A2B47) !important;
    margin: 0 !important;
    padding: 0 !important;
    display: block !important;
}

.page-title + .stCaption, 
.page-title + p {
    margin-bottom: 0.32rem !important;
}

.page-title + .stCaption + .stCaption {
    margin-top: 0.05rem !important;
    margin-bottom: 0.18rem !important;
}

[data-testid="stVerticalBlock"] {
    gap: 0.4rem !important;
}

[data-testid="stHorizontalBlock"] {
    gap: 0.5rem !important;
}

[data-testid="column"] {
    padding: 0 !important;
}
div[data-testid="stVerticalBlock"][class*="st-key-dashboard-card-"] {
    box-sizing: border-box !important;
    padding: 12px 12px 8px !important;
    background: #FFFFFF !important;
    border: 1px solid #D6E0EA !important;
    border-radius: 18px !important;
    box-shadow: 0 6px 18px rgba(10, 43, 71, 0.06) !important;
}

div[data-testid="stVerticalBlock"][class*="st-key-dashboard-card-"] > div {
    box-sizing: border-box !important;
    padding: 0 !important;
    background: #FFFFFF !important;
}

div[data-testid="stVerticalBlock"][class*="st-key-dashboard-card-"] [data-testid="stVerticalBlock"] {
    gap: 0.14rem !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071E33 0%, #041423 100%) !important;
    border-right: 1px solid rgba(0, 168, 181, 0.15) !important;
}

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.4rem !important;
    padding-left: 0.8rem !important;
    padding-right: 0.8rem !important;
}
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 0.48rem !important;
}

section[data-testid="stSidebar"] {
    overflow-y: auto !important;
    scrollbar-width: none !important;
}

section[data-testid="stSidebar"]::-webkit-scrollbar {
    display: none !important;
}

.sidebar-brand-wrapper {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 10px 16px 14px;
    margin-top: 0 !important;
    margin-bottom: 1.85rem !important;
    position: relative;
    overflow: hidden;
}

.sidebar-brand-wrapper::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: var(--accent);
}

.sidebar-title {
    font-size: 1.4rem !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    margin: 0 !important;
    line-height: 1.2 !important;
    letter-spacing: -0.02em;
}

.sidebar-subtitle {
    font-size: 0.72rem;
    color: #8CA0B3;
    font-weight: 600;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.sidebar-filter-heading {
    color: #00A8B5 !important;
    font-size: 1.25rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase;
    margin: 0.5rem 0 0.55rem 0.2rem !important;
}

.sidebar-comparison-status {
    display: none !important;
}

section[data-testid="stSidebar"] label p,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: #C2D5E5 !important;
    font-size: 0.80rem !important;
    font-weight: 700 !important;
}

.sidebar-filter-summary {
    font-size: 0.78rem;
    color: #E6FBFA;
    font-weight: 700;
    margin-top: 0.3rem;
    margin-bottom: 0.4rem;
}

section[data-testid="stSidebar"] .st-key-month_grid,
section[data-testid="stSidebar"] .st-key-quarter_grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 4px !important;
    margin-bottom: 0.5rem !important;
}

section[data-testid="stSidebar"] .st-key-month_grid .stButton,
section[data-testid="stSidebar"] .st-key-quarter_grid .stButton {
    width: 100% !important;
    margin: 0 !important;
}

section[data-testid="stSidebar"] .st-key-month_grid .stButton > button,
section[data-testid="stSidebar"] .st-key-quarter_grid .stButton > button {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.09) !important;
    border-radius: 6px !important;
    color: #A3B8CC !important;
    font-size: 0.70rem !important;
    font-weight: 700 !important;
    padding: 0.22rem 0 !important;
    min-height: 1.6rem !important;
    transition: all 0.2s ease !important;
}

section[data-testid="stSidebar"] .st-key-month_grid .stButton > button:hover,
section[data-testid="stSidebar"] .st-key-quarter_grid .stButton > button:hover {
    background: rgba(0, 168, 181, 0.15) !important;
    border-color: rgba(0, 168, 181, 0.4) !important;
    color: #FFFFFF !important;
    transform: translateY(-1px);
}

section[data-testid="stSidebar"] .st-key-month_grid button[kind="primary"],
section[data-testid="stSidebar"] .st-key-quarter_grid button[kind="primary"] {
    background: linear-gradient(135deg, #00A8B5 0%, #00828C 100%) !important;
    border: none !important;
    color: #FFFFFF !important;
    font-weight: 800 !important;
    box-shadow: 0 4px 10px rgba(0, 168, 181, 0.35) !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: rgba(10, 35, 58, 0.7) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 10px !important;
    color: #FFFFFF !important;
    font-size: 0.82rem !important;
    min-height: 2.1rem !important;
    transition: all 0.2s ease !important;
}

section[data-testid="stSidebar"] div[data-testid="stSelectbox"] {
    margin-bottom: 0.15rem !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover,
section[data-testid="stSidebar"] div[data-baseweb="select"] > div:focus {
    border-color: #00A8B5 !important;
    background: rgba(14, 45, 74, 0.9) !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] span {
    color: #E6FBFA !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] svg {
    fill: #00A8B5 !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child {
    border-color: rgba(255, 255, 255, 0.2) !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] label[data-baseweb="radio"] div:first-child div {
    background: var(--accent) !important;
}

section[data-testid="stSidebar"] .filter-item:hover {
    color: var(--accent) !important;
}

section[data-testid="stSidebar"] .stButton > button:not(.st-key-month_grid button):not(.st-key-quarter_grid button) {
    background: rgba(220, 38, 38, 0.08) !important;
    border: 1px solid rgba(220, 38, 38, 0.25) !important;
    color: #F87171 !important;
    border-radius: 999px !important;
    font-weight: 700 !important;
    font-size: 0.70rem !important;
    padding: 0.18rem 0.7rem !important;
    width: auto !important;
    min-height: 0 !important;
    transition: all 0.2s ease !important;
}

section[data-testid="stSidebar"] .stButton > button:not(.st-key-month_grid button):not(.st-key-quarter_grid button):hover {
    background: rgba(220, 38, 38, 0.25) !important;
    border-color: #EF4444 !important;
    color: #FFFFFF !important;
}

.st-key-kpi_section [data-testid="stHorizontalBlock"] {
    gap: 0.3rem !important;
}

div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #D0DFEE !important;
    border-top: 4px solid #0F2E4F !important;
    border-radius: 8px !important;
    padding: 10px 6px !important;
    height: 98px !important;
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
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
}

div[data-testid="stMetricLabel"] {
    white-space: normal !important;
    line-height: 1.15 !important;
    max-height: 2.3em !important;
    overflow: hidden !important;
    margin-bottom: 4px !important;
}

div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] > div,
div[data-testid="stMetricValue"] span {
    font-size: clamp(13px, 1.5vw, 21px) !important;
    font-weight: 800 !important;
    color: #0F2E4F !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    white-space: nowrap !important;
    line-height: 1.1 !important;
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
    padding: 1px 5px !important;
    border-radius: 6px !important;
}

div[data-testid="stMetricDelta"] > div[aria-label*="decrease"] {
    background-color: #FCE8E6 !important;
    color: #C5221F !important;
    padding: 1px 5px !important;
    border-radius: 6px !important;
}

.section-title {
    box-sizing: border-box;
    min-height: 25px;
    font-size: 15.5px;
    line-height: 19px;
    font-weight: 800;
    color: var(--navy) !important;
    margin: 0 0 6px;
    padding: 0 0 3px;
    border-bottom: 3px solid DCEFFA;
}

.section-title--large { font-size: 15.5px; }

.mini-section-title {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    color: #6787A5;
    margin-bottom: .2rem;
}
section[data-testid="stSidebar"] .mini-section-title {
    font-size: 11.5px !important;
    font-weight: 800 !important;
    letter-spacing: 0.06em !important;
    margin-bottom: .55rem !important;
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

div[data-testid="stVerticalBlock"][class*="st-key-dashboard-card-"] div[data-testid="stRadio"] {
    margin-bottom: 0.1rem !important;
}

div[data-testid="stVerticalBlock"][class*="st-key-dashboard-card-"] div[data-testid="stRadio"] > div {
    gap: 0.7rem !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

div[data-testid="stVerticalBlock"][class*="st-key-dashboard-card-"] div[data-testid="stRadio"] label {
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    color: #245274 !important;
    gap: 0.25rem !important;
    padding: 0 !important;
}

.gauge-pair{
    display:flex !important;
    justify-content:center !important;
    align-items:flex-start !important;
    width:100% !important;
    height:135px !important;
    gap:42px !important;
    padding:0 !important;
    margin:0 auto !important;
    box-sizing:border-box !important;
}

.gauge-block{
    width:200px !important;
    min-width:200px !important;
    max-width:200px !important;
    display:flex !important;
    flex-direction:column !important;
    align-items:center !important;
    justify-content:flex-start !important;
    box-sizing:border-box !important;
}

.gauge-block .mini-section-title{
    width:100% !important;
    margin:0 0 6px 0 !important;
    padding:6px 0 !important;
    text-align:center !important;
    font-size:11px !important;
    font-weight:800 !important;
    color:#6787A5 !important;
    line-height:1.1 !important;
}

.gauge-half-wrap{
    width:180px !important;
    height:90px !important;
    margin:0 auto !important;
    padding:0 !important;
    display:flex !important;
    justify-content:center !important;
    align-items:center !important;
    overflow:hidden !important;
    box-sizing:border-box !important;
}

.gauge-half{
    display:block !important;
    width:180px !important;
    height:90px !important;
}

.gauge-legend-row{
    width:100% !important;
    display:flex !important;
    justify-content:center !important;
    align-items:center !important;
    gap:10px !important;
    margin-top:6px !important;
    flex-wrap:nowrap !important;
}

.gauge-legend-item{
    font-size:12px !important;
    font-weight:800 !important;
    white-space:nowrap !important;
}

.chart-empty-message{
    text-align:center !important;
    padding-top:1rem !important;
}

.donut-chart {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 4rem !important;               
    width: 100% !important;
    height: 160px !important;
    min-height: 160px !important;
    flex: 0 0 160px !important;
    padding: 0 !important;
}

.donut-chart-circle {
    width: 140px !important;
    height: 140px !important;
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

.donut-slice {
    cursor: pointer;
}

.donut-slice--0, .donut-chart-color--0 { stroke: #0A2B47; background: #0A2B47; }
.donut-slice--1, .donut-chart-color--1 { stroke: #123C5D; background: #123C5D; }
.donut-slice--2, .donut-chart-color--2 { stroke: #1E3A5F; background: #1E3A5F; }
.donut-slice--3, .donut-chart-color--3 { stroke: #2F5A82; background: #2F5A82; }
.donut-slice--4, .donut-chart-color--4 { stroke: #00A8B5; background: #00A8B5; }
.donut-slice--5, .donut-chart-color--5 { stroke: #3FBEC9; background: #3FBEC9; }
.donut-slice--6, .donut-chart-color--6 { stroke: #7CC6D6; background: #7CC6D6; }
.donut-slice--7, .donut-chart-color--7 { stroke: #ABDBE4; background: #ABDBE4; }
.donut-slice--8, .donut-chart-color--8 { stroke: #CDE8EC; background: #CDE8EC; }

.donut-chart-center {
    width: 76px !important;
    height: 76px !important;
    border-radius: 50% !important;
    background: #FFFFFF !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 2px 8px rgba(0,0,0,.08) !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
}

.donut-chart-legend {
    flex: 1 !important;
    min-width: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    gap: 0.28rem !important;
    align-self: stretch !important;
    height: 100% !important;
    max-height: 100% !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    box-sizing: border-box !important;
    padding-top: 4px !important;
    padding-right: 0.2rem !important;
}

.donut-chart-row {
    display: grid !important;
    grid-template-columns: 12px minmax(0, 1fr) !important;
    align-items: start !important;
    gap: 0.5rem !important;
    min-height: 26px !important;
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

div[data-testid="stVerticalBlock"].st-key-dashboard-card-gauge:has(.gauge-pair),
div[data-testid="stVerticalBlock"].st-key-dashboard-card-donut:has(.donut-chart) {
    display: flex !important;
    flex-direction: column !important;
}

div[data-testid="stVerticalBlock"].st-key-dashboard-card-donut:has(.city-rank-card),
div[data-testid="stVerticalBlock"].st-key-dashboard-card-customer:has(.city-rank-card),
div[data-testid="stVerticalBlock"].st-key-dashboard-card-city:has(.city-rank-card) {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    height: 100% !important;
}

div[data-testid="stVerticalBlock"].st-key-dashboard-card-donut [data-testid="stElementContainer"]:has(.city-rank-card),
div[data-testid="stVerticalBlock"].st-key-dashboard-card-customer [data-testid="stElementContainer"]:has(.city-rank-card),
div[data-testid="stVerticalBlock"].st-key-dashboard-card-city [data-testid="stElementContainer"]:has(.city-rank-card) {
    display: flex !important;
    width: 100% !important;
    align-items: center !important;
    justify-content: center !important;
}

div[data-testid="stVerticalBlock"].st-key-dashboard-card-gauge [data-testid="stElementContainer"]:has(.gauge-pair),
div[data-testid="stVerticalBlock"].st-key-dashboard-card-donut [data-testid="stElementContainer"]:has(.donut-chart) {
    display: flex !important;
    flex: 1 !important;
    min-height: 0 !important;
}

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
    padding: 0.18rem 0;
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
div[data-testid="stElementToolbar"] {
    display: none !important;
}

.city-rank-card {
    background: linear-gradient(180deg, #FFFFFF 0%, #F7FBFF 100%) !important;
    border: 1px solid rgba(10, 43, 71, 0.10) !important;
    border-radius: 18px !important;
    padding: 14px 16px !important;
    width: 100% !important;
    max-width: 420px !important; 
    box-sizing: border-box !important;
    margin: auto !important; 
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    align-items: stretch !important;
    text-align: left !important;
    box-shadow: 0 16px 34px rgba(4, 23, 38, 0.08) !important;
    position: relative !important;
    overflow: hidden !important;
}

.city-rank-card::before {
    content: '' !important;
    position: absolute !important;
    left: 0 !important;
    right: 0 !important;
    top: 0 !important;
    height: 4px !important;
    background: linear-gradient(90deg, #0A2B47 0%, #00A8B5 100%) !important;
}

.city-rank-title {
    font-size: 0.70rem !important;
    font-weight: 800 !important;
    color: #6787A5 !important;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.24rem !important;
    z-index: 2 !important;
}

.city-rank-number {
    font-size: 1.95rem !important;
    font-weight: 900 !important;
    color: #0A2B47 !important;
    line-height: 1 !important;
    display: flex !important;
    align-items: baseline !important;
    justify-content: flex-start !important;
    gap: 4px !important;
    margin: 0.05rem 0 0.14rem !important;
    z-index: 2 !important;
}

.city-rank-number span {
    font-size: 0.78rem !important;
    color: #8CA0B3 !important;
    font-weight: 700 !important;
}

.city-rank-sparkline-wrap {
    width: 100% !important;
    height: 40px !important;
    margin: 0.2rem 0 0.15rem !important;
    z-index: 1 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
}

.city-rank-sparkline-wrap svg {
    width: 100% !important;
    height: 100% !important;
    overflow: visible !important;
}

.city-rank-benchmark {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 5px !important;
    font-size: 0.70rem !important;
    font-weight: 800 !important;
    padding: 5px 11px !important;
    border-radius: 999px !important;
    white-space: nowrap !important;
    z-index: 2 !important;
    margin-top: 0.1rem !important;
    align-self: flex-start !important;
}

.benchmark-up {
    color: #137333 !important;
    background-color: #E6F4EA !important;
}

.benchmark-down {
    color: #C5221F !important;
    background-color: #FCE8E6 !important;
}

.benchmark-icon {
    font-size: 0.85rem !important;
    font-weight: 900 !important;
}

div[data-testid="stVerticalBlock"].st-key-dashboard-card-donut .city-rank-card svg,
div[data-testid="stVerticalBlock"].st-key-dashboard-card-customer .city-rank-card svg,
div[data-testid="stVerticalBlock"].st-key-dashboard-card-city .city-rank-card svg {
    opacity: 0.95;
}

div[data-testid="stVerticalBlock"].st-key-dashboard-card-donut .city-rank-card strong,
div[data-testid="stVerticalBlock"].st-key-dashboard-card-customer .city-rank-card strong,
div[data-testid="stVerticalBlock"].st-key-dashboard-card-city .city-rank-card strong {
    font-weight: 800 !important;
}

@media (max-width: 860px) {
    .city-rank-card {
        max-width: none !important;
        padding: 13px 14px !important;
        border-radius: 16px !important;
    }

    .city-rank-title {
        font-size: 0.68rem !important;
        letter-spacing: 0.10em;
    }

    .city-rank-number {
        font-size: 1.78rem !important;
    }

    .city-rank-sparkline-wrap {
        height: 38px !important;
    }

    .city-rank-benchmark {
        white-space: normal !important;
        line-height: 1.2 !important;
    }
}

@media (max-width: 560px) {
    .city-rank-card {
        padding: 12px 12px !important;
    }

    .city-rank-number {
        font-size: 1.65rem !important;
    }

    .city-rank-number span {
        font-size: 0.74rem !important;
    }

    .city-rank-benchmark {
        font-size: 0.66rem !important;
        padding: 4px 10px !important;
    }
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