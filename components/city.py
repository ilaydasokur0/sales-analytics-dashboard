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

