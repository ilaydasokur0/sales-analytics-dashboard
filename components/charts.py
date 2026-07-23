import streamlit as st
import services.analysis as sa
import pandas as pd
from components.kpi import render_share_metrics
from utils.metrics import get_amount_share
import html
import textwrap

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

def build_selected_product_info(filtered_df):
    if filtered_df.empty:
        return []

    product_row = filtered_df.iloc[0]
    info_items = [
        ("Ürün Adı", product_row.get("product_name", "-")),
        ("PL Durumu", product_row.get("pl_status", "-")),
        ("Ürün Tipi", product_row.get("product_type", "-")),
        ("ADT", product_row.get("unit", "-")),
        ("Ürün Kodu", product_row.get("product_id", "-")),
    ]

    return info_items


def render_product_info_card(filtered_df):
    info_items = build_selected_product_info(filtered_df)
    if not info_items:
        st.info("Veri bulunamadı.")
        return

    for index, (label, value) in enumerate(info_items):
        left_col, right_col = st.columns([1, 1.1], gap="small")

        with left_col:
            st.markdown(
                f'<div class="product-info-label">{label}</div>',
                unsafe_allow_html=True,
            )

        with right_col:
            st.markdown(
                f'<div class="product-info-value">{value}</div>',
                unsafe_allow_html=True,
            )

        if index != len(info_items) - 1:
            st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)


def render_chart_section(filtered_df, active_filters):
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
            city_selected = active_filters["city"] != "Hepsi"
            customer_selected = active_filters["customer"] != "Hepsi"
            product_selected = active_filters.get("product", "Hepsi") != "Hepsi"

            if city_selected and customer_selected and product_selected:
                st.markdown('<div class="section-title section-title--large">Ürün Özellikleri</div>', unsafe_allow_html=True)
                render_product_info_card(filtered_df)
            else:
                st.markdown('<div class="section-title section-title--large">Dağılımlar</div>', unsafe_allow_html=True)

                st.markdown('<div class="mini-section-title">PL Dağılımı</div>', unsafe_allow_html=True)
                render_share_metrics(get_amount_share(filtered_df, "pl_status"))

                st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)

                st.markdown('<div class="mini-section-title">Ürün Dağılımı</div>', unsafe_allow_html=True)
                render_share_metrics(get_amount_share(filtered_df, "product_type"))




def render_horizontal_bar_chart(
    title,
    chart_df,
    label_col,
    value_col,
    value_suffix="",
    empty_message="Veri bulunamadı.",
):
    st.markdown(
        f'<div class="section-title section-title--large">{title}</div>',
        unsafe_allow_html=True,
    )

    if chart_df.empty:
        st.info(empty_message)
        return

    max_value = chart_df[value_col].max()

    for _, row in chart_df.iterrows():
        label = html.escape(str(row[label_col]))
        value = float(row[value_col])

        width = 0
        if max_value != 0:
            width = (value / max_value) * 100

        st.markdown(
            textwrap.dedent(f"""
                <div class="horizontal-bar-row">
                    <div class="horizontal-bar-name" title="{label}">{label}</div>
                    <div class="horizontal-bar-track">
                        <div class="horizontal-bar-bar" style="width:{width:.1f}%;"></div>
                    </div>
                    <div class="horizontal-bar-meta">
                        <div class="horizontal-bar-amount">{value:,.0f}{value_suffix}</div>
                    </div>
                </div>
            """).strip(),
            unsafe_allow_html=True,
        )

def render_donut_chart(title, chart_df, label_col, value_col, empty_message="Veri bulunamadı."):
    st.markdown(
        f'<div class="section-title section-title--large">{title}</div>',
        unsafe_allow_html=True,
    )
    if chart_df.empty:
        st.info(empty_message)
        return

    for _, row in chart_df.iterrows():
        label = html.escape(str(row[label_col]))
        value = float(row[value_col])

        st.markdown(
            textwrap.dedent(f"""
                <div class="donut-chart-row">
                    <div class="donut-chart-label">{label}</div>
                    <div class="donut-chart-value">{value:,.0f}</div>
                </div>
            """).strip(),
            unsafe_allow_html=True,
        )
    
