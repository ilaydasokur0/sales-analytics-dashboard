import pandas as pd
import streamlit as st
from services.dashboard_data import prepare_dashboard_data, get_month_comparison_frames
from styles import load_css
import services.analysis as sa
from components.sidebar import apply_sidebar_filters
from components.overview import render_dashboard_body, render_header
from components.kpi import render_kpi_section

# ---------------- SAYFA ---------------- #

st.set_page_config(
    page_title="Satış Raporu",
    page_icon="📊",
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

# Veriyi hazırlama
(
    current_month_df,
    previous_month_df,
    national_df,
    national_summary_df,
    national_previous_df,
    city_base_df,
    city_and_customer_selected,
    city_and_customer_and_product_selected,
) = prepare_dashboard_data(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
    current_month_df,
    previous_month_df,
)

# İl/Müşteri/Ürün filtreli fakat tarih (ay) filtresiz veri seti: Aylık
# Performans grafiğinde tek ay seçildiğinde komşu ayları bağlam olarak
# (soluk) göstermek için kullanılır.
monthly_chart_df = sa.filter_data(
    sales_df,
    city=None if active_filters["city"] == "Hepsi" else active_filters["city"],
    customer=None if active_filters["customer"] == "Hepsi" else active_filters["customer"],
    product=None if active_filters["product"] == "Hepsi" else active_filters["product"],
)

render_header(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
    current_month_df,
)

render_kpi_section(
    current_month_df,
    previous_month_df,
    city_base_df,
    national_df,
    active_filters,
    comparison_enabled,
)

# ---------------- DASHBOARD GÖVDESİ (Gauge + Donut + Performans) ---------------- #

render_dashboard_body(
    current_month_df,
    active_filters,
    monthly_chart_df=monthly_chart_df,
)