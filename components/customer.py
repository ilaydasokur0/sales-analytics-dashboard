import streamlit as st

from components.charts import render_horizontal_bar_chart
from utils.tables import build_ranked_table


def render_customer_product_ranking(current_df):
    chart_df = build_ranked_table(
        current_df,
        "product_name",
        "quantity",
        group_label="Ürün",
        value_label="Kilogram",
    )

    with st.container(height=320):
        render_horizontal_bar_chart(
            title="Ürün Sıralaması",
            chart_df=chart_df,
            label_col="Ürün",
            value_col="Kilogram",
        )

def render_customer_invoice_summary(avg_invoice, difference, status):
    icon = "▲" if status == "Üzerinde" else "▼"
    benchmark_class = "benchmark-up" if status == "Üzerinde" else "benchmark-down"
    line_color = "#16A34A" if status == "Üzerinde" else "#DC2626"

    st.markdown(
        f"""
        <div class="city-rank-card">
            <div class="city-rank-title">Müşterİnİn Ortalama Fatura Tutarı</div>
            <div class="city-rank-number">₺{avg_invoice:,.0f}</div>
            <div class="city-rank-sparkline-wrap">
                <svg viewBox="0 0 200 50" preserveAspectRatio="none">
                    <defs>
                        <linearGradient id="sparklineGradCustInv" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="0%" stop-color="{line_color}" stop-opacity="0.25" />
                            <stop offset="100%" stop-color="{line_color}" stop-opacity="0.0" />
                        </linearGradient>
                    </defs>
                    <path d="M0,35 Q30,15 60,30 T120,10 T180,38 T200,20 L200,50 L0,50 Z" fill="url(#sparklineGradCustInv)" />
                    <path d="M0,35 Q30,15 60,30 T120,10 T180,38 T200,20" fill="none" stroke="{line_color}" stroke-width="2.5" stroke-linecap="round" />
                </svg>
            </div>
            <div class="city-rank-benchmark {benchmark_class}">
                <span class="benchmark-icon">{icon}</span><span>Genel ortalamanın <strong>%{difference:.1f}</strong> {status.lower()}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )