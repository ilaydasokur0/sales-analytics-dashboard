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

def render_customer_invoice_summary(avg_invoice, difference, status):

    icon = "▲" if status == "Üzerinde" else "▼"
    benchmark_class = "benchmark-up" if status == "Üzerinde" else "benchmark-down"

    st.markdown(
        f"""
        <div class="city-rank-card">
            <div class="city-rank-title">Müşterinin Ortalama Fatura Tutarı</div>
            <div class="city-rank-number">₺{avg_invoice:,.0f}</div>
            <div class="city-rank-benchmark {benchmark_class}">
            <span class="benchmark-icon">{icon}</span><span>Genel ortalamanın <strong>%{difference:.1f}</strong> {status.lower()}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
