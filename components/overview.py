import streamlit as st

from components.charts import render_donut_chart, render_horizontal_bar_chart
from components.city import (
    render_city_customer_product_ranking,
    render_customer_revenue_share_chart,
    render_city_product_tables,
)
from components.customer import render_customer_product_ranking
from components.general import render_overview_section
from components.product import render_product_detail_table
from utils.tables import build_product_revenue_share_table, build_ranked_table


def render_header(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
    current_month_df,
):
    st.markdown('<div class="page-title">Satış Raporu</div>', unsafe_allow_html=True)

    filter_summary = []
    if active_filters["city"] != "Hepsi":
        filter_summary.append(f"İl: {active_filters['city']}")
    if active_filters["customer"] != "Hepsi":
        filter_summary.append(f"Müşteri: {active_filters['customer']}")
    if active_filters["product"] != "Hepsi":
        filter_summary.append(f"Ürün: {active_filters['product']}")
    filter_summary.insert(
        0,
        f"Tarih: {active_filters['start_date']} - {active_filters['end_date']}",
    )

    if comparison_enabled:
        st.caption(f"Karşılaştırma: {current_period} / {previous_period}")
    elif (
        active_filters["start_date"] == sales_df["invoice_date"].min().date()
        and active_filters["end_date"] == sales_df["invoice_date"].max().date()
    ):
        st.caption("Seçilen tarih aralığı için karşılaştırma yapılamıyor.")

    if current_month_df.empty:
        st.warning("Seçilen filtrelerde veri bulunamadı. Filtreleri genişletip tekrar deneyin.")
        st.stop()

    st.caption(" | ".join(filter_summary) if filter_summary else "Seçilen filtre: yok")


def render_compact_overview_tables(
    current_df,
    previous_df,
    *,
    city_selected,
    customer_selected,
    product_selected,
    city_summary_df,
    national_summary_df,
    national_current_df=None,
    national_previous_df=None,
    selected_city=None,
    comparison_enabled=True,
):
    if city_selected and customer_selected and product_selected:
        st.header("Ürün Performansı")
        render_product_detail_table(current_df)
        return

    if city_selected and customer_selected:
        render_city_customer_product_ranking(current_df)
        return

    if customer_selected:
        render_customer_product_ranking(current_df)
        return

    if city_selected:
        st.header("İl Özeti")
        col1, col2 = st.columns([1.28, 1.22], gap="large")
        with col1:
            render_customer_revenue_share_chart(current_df)
        with col2:
            render_city_product_tables(current_df, previous_df)
        return

    st.header("Performans Özeti")
    col1, col2, col3 = st.columns(3)

    with col1:
        customer_ranking = build_ranked_table(
            current_df,
            "customer_name",
            "total_amount",
            group_label="Müşteri",
            value_label="Ciro",
        )
        with st.container(height=320):
            render_horizontal_bar_chart(
                title="Müşteri Performansı",
                chart_df=customer_ranking,
                label_col="Müşteri",
                value_col="Ciro",
                value_suffix=" ₺",
            )

    with col2:
        city_ranking = build_ranked_table(
            current_df,
            "city",
            "total_amount",
            group_label="İl",
            value_label="Ciro",
        )
        with st.container(height=320):
            render_horizontal_bar_chart(
                title="Bölgesel Performans",
                chart_df=city_ranking,
                label_col="İl",
                value_col="Ciro",
                value_suffix=" ₺",
            )

    with col3:
        render_donut_chart(
            title="Ürün Payları",
            chart_df=build_product_revenue_share_table(current_df),
            label_col="product_name",
            value_col="total_amount",
        )