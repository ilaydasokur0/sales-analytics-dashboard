import streamlit as st
from components.city import render_city_summary_cards, render_city_product_tables
from components.product import render_product_detail_table
from components.general import render_overview_section
import analysis as sa
from utils.metrics import get_month_comparison_frames


def render_header(sales_df, active_filters, comparison_enabled, current_period, previous_period):
    st.markdown('<div class="page-title">Satış Raporu</div>', unsafe_allow_html=True)

    #Filtrelerin özetini oluşturur
    filter_summary = []
    if active_filters["city"] != "Hepsi":
        filter_summary.append(f"İl: {active_filters['city']}")
    if active_filters["customer"] != "Hepsi":
        filter_summary.append(f"Müşteri: {active_filters['customer']}")
    if active_filters["product"] != "Hepsi":
        filter_summary.append(f"Ürün: {active_filters['product']}")

    # Karşılaştırma için geçerli ay ve önceki ay verilerini alır
    current_month_df, previous_month_df, comparison_enabled_local, current_period_local, previous_period_local = get_month_comparison_frames(
        sales_df, active_filters
    )

    # Ulusal bazlı verileri filtreler 
    national_df = sa.filter_data(
        sales_df,
        customer=None if active_filters["customer"] == "Hepsi" else active_filters["customer"],
        product=None if active_filters["product"] == "Hepsi" else active_filters["product"],
        start_date=active_filters["start_date"],
        end_date=active_filters["end_date"],
    )
    national_summary_df = national_df.copy()
    if comparison_enabled:
        national_df = national_df[national_df["invoice_date"].dt.to_period("M") == current_period]

    # Önceki ay verilerini alır (karşılaştırma etkinse)
    national_previous_df = (
        national_summary_df[national_summary_df["invoice_date"].dt.to_period("M") == previous_period]
        if comparison_enabled and previous_period is not None
        else national_summary_df.iloc[0:0]
    )
    
    city_and_customer_selected = (
        active_filters["city"] != "Hepsi" and active_filters["customer"] != "Hepsi"
    )

    # İl bazlı verileri filtreler
    city_base_df = sa.filter_data(
        sales_df,
        city=None if active_filters["city"] == "Hepsi" else active_filters["city"],
        product=None if active_filters["product"] == "Hepsi" else active_filters["product"],
        start_date=active_filters["start_date"],
        end_date=active_filters["end_date"],
    )
    if comparison_enabled:
        city_base_df = city_base_df[city_base_df["invoice_date"].dt.to_period("M") == current_period]
    
    filter_summary.insert(0, f"Tarih: {active_filters['start_date']} - {active_filters['end_date']}")
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

    return (
        current_month_df,
        previous_month_df,
        national_df,
        national_summary_df,
        national_previous_df,
        city_base_df,
        city_and_customer_selected,
    )


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
        col1, col2 = st.columns([1, 2])

        with col1:
            render_city_summary_cards(
                selected_city,
                current_df,
                previous_df,
                national_current_df,
                national_previous_df,
                comparison_enabled,
            )

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
