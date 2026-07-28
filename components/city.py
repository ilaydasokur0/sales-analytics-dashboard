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

def render_city_summary_rank(rank, total, share):
    progress = ((total - rank + 1) / total) * 100

    html = (
        f'<div class="city-rank-card">'
        f'<div class="city-rank-title">Türkiye Geneli</div>'
        f'<div class="city-rank-number">{rank} / {total}</div>'
        f'<div class="city-rank-progress">'
        f'<div class="city-rank-progress-fill" style="width:{progress:.1f}%;"></div>'
        f"</div>"
        f'<div class="city-rank-share">Toplam cironun <span>%{share:.1f}</span>\'ini oluşturuyor.</div>'
        f"</div>"
    )

    st.markdown(html, unsafe_allow_html=True)