import pandas as pd
import streamlit as st
from styles import load_css
import analysis as sa
from components.sidebar import apply_sidebar_filters
from components.overview_clean import render_compact_overview_tables, render_header
from components.general import render_ranked_pair
from components.kpi import render_kpi_section
from components.charts import render_chart_section
from utils.metrics import get_month_comparison_frames

# ---------------- SAYFA ---------------- #

st.set_page_config(
    page_title="Satış Dashboard",
    layout="wide",
)

# ---------------- VERİ ---------------- #
load_css()

@st.cache_data(show_spinner=False)
def get_sales_data():
    return sa.load_data()


try:
    sales_df = get_sales_data()
except (FileNotFoundError, KeyError, pd.errors.ParserError) as error:
    st.error(f"Veri dosyaları yüklenemedi: {error}")
    st.stop()

# ---------------- FİLTRELER ---------------- #

filtered_df, active_filters = apply_sidebar_filters(sales_df)

# ---------------- SAYFA ---------------- #

# Compute comparison frames (used by header and downstream sections)
current_month_df, previous_month_df, comparison_enabled, current_period, previous_period = get_month_comparison_frames(
    sales_df, active_filters
)

# Render header (title, filter summary, captions, and no-data warning)
(
    current_month_df,
    previous_month_df,
    national_df,
    national_summary_df,
    national_previous_df,
    city_base_df,
    city_and_customer_selected,
) = render_header(sales_df, active_filters, comparison_enabled, current_period, previous_period)

render_kpi_section(
    current_month_df,
    previous_month_df,
    city_base_df,
    national_df,
    active_filters,
    comparison_enabled,
)

st.markdown('<div style="height:.35rem"></div>', unsafe_allow_html=True)

# ---------------- GRAFİK + DAĞILIMLAR ---------------- #

render_chart_section(filtered_df)

# ---------------- ÖNE ÇIKANLAR ---------------- #

render_compact_overview_tables(
    current_month_df,
    previous_month_df,
    city_selected=active_filters["city"] != "Hepsi",
    customer_selected=active_filters["customer"] != "Hepsi",
    product_selected=active_filters["product"] != "Hepsi",
    city_summary_df=filtered_df,
    national_summary_df=national_summary_df,
    national_current_df=national_df,
    national_previous_df=national_previous_df,
    selected_city=None if active_filters["city"] == "Hepsi" else active_filters["city"],
    comparison_enabled=comparison_enabled,
)