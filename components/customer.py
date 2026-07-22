import streamlit as st

from components.charts import render_horizontal_bar_chart
from utils.tables import build_ranked_table


def render_customer_product_ranking(current_df):
    chart_df = build_ranked_table(
        current_df,
        "product_name",
        "quantity",
        group_label="Ürün",
        value_label="Satış Adedi",
    )

    with st.container(height=320):
        render_horizontal_bar_chart(
            title="Ürün Sıralaması",
            chart_df=chart_df,
            label_col="Ürün",
            value_col="Satış Adedi",
        )
