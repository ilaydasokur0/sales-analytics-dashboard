
from turtle import color

import streamlit as st
from components import charts
from services import analysis as sa
import html
from components.kpi import get_trend_arrow
from utils.tables import build_ranked_table, build_change_table
from utils.tables import build_customer_revenue_share_table

def render_customer_revenue_share_chart(current_df):
    chart_df = build_customer_revenue_share_table(current_df)

    charts.render_horizontal_bar_chart(
        title="Müşteri Ciro Payları",
        chart_df=chart_df,
        label_col="customer_name",
        value_col="share",
        value_suffix="%"
    )

def render_city_customer_product_ranking(current_df):
    chart_df = build_ranked_table(
        current_df,
        "product_name",
        "quantity",
        group_label="Ürün",
        value_label="Satış Adedi",
    )

    with st.container(height=320):
        charts.render_horizontal_bar_chart(
            title="Ürün Sıralaması",
            chart_df=chart_df,
            label_col="Ürün",
            value_col="Satış Adedi",
        )

def render_city_summary_rank(rank, total, difference, status):
    progress = ((total - rank + 1) / total) * 100

    icon = "▲" if status == "Üzerinde" else "▼"
    benchmark_class = "benchmark-up" if status == "Üzerinde" else "benchmark-down"

    st.markdown(
        f"""<div class="city-rank-card">
        <div class="city-rank-title">İlin Ulusal Ciro Sıralaması</div>
        <div class="city-rank-number">#{rank} <span>/{total}</span></div>
        <div class="city-rank-benchmark {benchmark_class}">
        <span class="benchmark-icon">{icon}</span>
        <span>Ulusal ortalamanın<strong>%{difference:.1f}</strong>{status.lower()}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
)