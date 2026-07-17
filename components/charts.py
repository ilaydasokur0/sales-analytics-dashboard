import streamlit as st
import analysis as sa

def render_chart_controls(graph_key):
    return st.radio(
        "Grafik Türü",
        ["Ciro", "Satış Adedi"],
        horizontal=True,
        key=graph_key,
        label_visibility="collapsed",
    )



def get_chart_data(df, graph_type):
    if graph_type == "Ciro":
        return sa.get_monthly_sales(df)

    return sa.get_monthly_quantity(df)


from components.kpi import render_share_metrics
from utils.metrics import get_amount_share


def render_chart_section(filtered_df):
    graph_col, dist_col = st.columns(2, gap="small")

    with graph_col:
        with st.container(border=True):
            st.markdown('<div class="section-title section-title--large">Aylık Performans Grafiği</div>', unsafe_allow_html=True)
            st.markdown('<div class="mini-section-title">Grafik Seçimi</div>', unsafe_allow_html=True)
            graph_type = render_chart_controls("general_graph")
            chart_data = get_chart_data(filtered_df, graph_type)
            st.line_chart(chart_data, width="stretch", height=200)

    with dist_col:
        with st.container(border=True):
            st.markdown('<div class="section-title section-title--large">Dağılımlar</div>', unsafe_allow_html=True)

            st.markdown('<div class="mini-section-title">PL Dağılımı</div>', unsafe_allow_html=True)
            render_share_metrics(get_amount_share(filtered_df, "pl_status"))

            st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)

            st.markdown('<div class="mini-section-title">Ürün Dağılımı</div>', unsafe_allow_html=True)
            render_share_metrics(get_amount_share(filtered_df, "product_type"))
