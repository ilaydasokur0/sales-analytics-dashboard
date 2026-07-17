import streamlit as st
from utils.tables import build_ranked_table, build_change_table
from components.city import render_city_summary_cards, render_city_product_tables
from components.customer import render_customer_city_product_table
import analysis as sa
from utils.metrics import get_month_comparison_frames


def render_ranked_pair(
    current_df,
    previous_df,
    left_title,
    right_title,
    *,
    group_col,
    value_col,
    group_label,
    value_label,
    currency=False,
    top_n=3,
    height=145,
):
    left_table = build_ranked_table(
        current_df,
        previous_df,
        group_col,
        value_col,
        top_n=top_n,
        ascending=False,
        group_label=group_label,
        value_label=value_label,
        currency=currency,
    )

    right_table = build_ranked_table(
        current_df,
        previous_df,
        group_col,
        value_col,
        top_n=top_n,
        ascending=True,
        group_label=group_label,
        value_label=value_label,
        currency=currency,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(left_title)
        st.dataframe(
            left_table,
            hide_index=True,
            width="stretch",
            height=height,
        )

    with col2:
        st.subheader(right_title)
        st.dataframe(
            right_table,
            hide_index=True,
            width="stretch",
            height=height,
        )


def render_header(sales_df, active_filters, comparison_enabled, current_period, previous_period):
    """Render page title, filter summary, comparison caption and no-data warning.

    Returns: (current_month_df, previous_month_df, national_df, national_summary_df, national_previous_df, city_base_df, city_and_customer_selected)
    """
    st.markdown('<div class="page-title">Satış Dashboard</div>', unsafe_allow_html=True)

    filter_summary = []
    if active_filters["city"] != "Hepsi":
        filter_summary.append(f"İl: {active_filters['city']}")
    if active_filters["customer"] != "Hepsi":
        filter_summary.append(f"Müşteri: {active_filters['customer']}")
    if active_filters["product"] != "Hepsi":
        filter_summary.append(f"Ürün: {active_filters['product']}")

    current_month_df, previous_month_df, comparison_enabled_local, current_period_local, previous_period_local = get_month_comparison_frames(
        sales_df, active_filters
    )

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

    national_previous_df = (
        national_summary_df[national_summary_df["invoice_date"].dt.to_period("M") == previous_period]
        if comparison_enabled and previous_period is not None
        else national_summary_df.iloc[0:0]
    )

    city_and_customer_selected = (
        active_filters["city"] != "Hepsi" and active_filters["customer"] != "Hepsi"
    )

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
        st.caption("Tüm tarih aralığı seçili: karşılaştırma yapılmıyor.")
    else:
        st.caption("Seçilen filtre için önceki dönem verisi bulunamadı.")

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



def render_full_overview_tables(current_df, previous_df):

    st.header("Performans Özeti")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Müşteri Performansı")
        customer_top = build_ranked_table(
            current_df,
            previous_df,
            "customer_name",
            "total_amount",
            top_n=3,
            ascending=False,
            group_label="Müşteri",
            value_label="Ciro",
            currency=True,
        )
        customer_bottom = build_change_table(
            current_df,
            previous_df,
            "customer_name",
            "total_amount",
            top_n=3,
            group_label="Müşteri",
            value_label="Ciro",
            currency=True,
        )

        st.caption("Lider Segmentler")
        st.dataframe(customer_top, hide_index=True, width="stretch", height=112)
        st.caption("Gelişim Alanları")
        st.dataframe(customer_bottom, hide_index=True, width="stretch", height=112)

    with col2:
        st.subheader("Bölgesel Performans")
        city_top = build_ranked_table(
            current_df,
            previous_df,
            "city",
            "total_amount",
            top_n=3,
            ascending=False,
            group_label="İl",
            value_label="Ciro",
            currency=True,
        )
        city_bottom = build_change_table(
            current_df,
            previous_df,
            "city",
            "total_amount",
            top_n=3,
            group_label="İl",
            value_label="Ciro",
            currency=True,
        )

        st.caption("Lider Segmentler")
        st.dataframe(city_top, hide_index=True, width="stretch", height=112)
        st.caption("Gelişim Alanları")
        st.dataframe(city_bottom, hide_index=True, width="stretch", height=112)

    with col3:
        st.subheader("Ürün Performansı")
        product_top = build_ranked_table(
            current_df,
            previous_df,
            "product_name",
            "quantity",
            top_n=3,
            ascending=False,
            group_label="Ürün",
            value_label="Satış Adedi",
        )
        product_bottom = build_change_table(
            current_df,
            previous_df,
            "product_name",
            "quantity",
            top_n=3,
            group_label="Ürün",
            value_label="Satış Adedi",
        )

        st.caption("Lider Segmentler")
        st.dataframe(product_top, hide_index=True, width="stretch", height=112)
        st.caption("Gelişim Alanları")
        st.dataframe(product_bottom, hide_index=True, width="stretch", height=112)



def render_overview_section(
    current_df,
    previous_df,
    title,
    group_col,
    value_col,
    group_label,
    value_label,
    *,
    currency=False,
    top_caption="Lider Segmentler",
    bottom_caption="Gelişim Alanları",
):
    st.subheader(title)
    top_table = build_ranked_table(
        current_df,
        previous_df,
        group_col,
        value_col,
        top_n=3,
        group_label=group_label,
        value_label=value_label,
        currency=currency,
    )
    change_table = build_change_table(
        current_df,
        previous_df,
        group_col,
        value_col,
        top_n=3,
        group_label=group_label,
        value_label=value_label,
        currency=currency,
    )
    st.caption(top_caption)
    st.dataframe(top_table, hide_index=True, width="stretch", height=112)
    st.caption(bottom_caption)
    st.dataframe(change_table, hide_index=True, width="stretch", height=112)


def render_compact_overview_tables(
    current_df,
    previous_df,
    *,
    city_selected,
    customer_selected,
    city_summary_df,
    national_summary_df,
    national_current_df=None,
    national_previous_df=None,
    selected_city=None,
    comparison_enabled=True,
):
    if city_selected and customer_selected:
        render_customer_city_product_table(current_df, previous_df)
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