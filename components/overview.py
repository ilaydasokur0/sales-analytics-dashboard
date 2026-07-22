import streamlit as st
from components.city import render_customer_revenue_share_chart, render_city_product_tables
from components.product import render_product_detail_table
from components.general import render_overview_section
import services.analysis as sa
from utils.metrics import get_month_comparison_frames


def render_header(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
    current_month_df,
):
    st.markdown('<div class="page-title">Satış Raporu</div>', unsafe_allow_html=True)

    # Filtre özetini oluştur
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

    # Karşılaştırma bilgisini göster
    if comparison_enabled:
        st.caption(f"Karşılaştırma: {current_period} / {previous_period}")

    elif (
        active_filters["start_date"] == sales_df["invoice_date"].min().date()
        and active_filters["end_date"] == sales_df["invoice_date"].max().date()
    ):
        st.caption("Seçilen tarih aralığı için karşılaştırma yapılamıyor.")

    # Veri yoksa kullanıcıyı uyar
    if current_month_df.empty:
        st.warning("Seçilen filtrelerde veri bulunamadı. Filtreleri genişletip tekrar deneyin.")
        st.stop()

    # Filtre özetini göster
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
        render_city_product_tables(current_df, previous_df)
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
        render_overview_section(
            current_df, previous_df, "Müşteri Performansı", "customer_name", "total_amount",
            "Müşteri", "Ciro", currency=True,
        )

    with col2:
        render_overview_section(
            current_df, previous_df, "Bölgesel Performans", "city", "total_amount",
            "İl", "Ciro", currency=True,
        )

    with col3:
        render_overview_section(
            current_df, previous_df, "Ürün Performansı", "product_name", "quantity",
            "Ürün", "Satış Adedi",
            top_caption="En Çok Satılan Ürünler",
            bottom_caption="En Çok Düşüş Yaşayan Ürünler",
        )
