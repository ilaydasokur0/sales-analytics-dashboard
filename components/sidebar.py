import pandas as pd
import streamlit as st

from services import analysis as sa


FILTER_WIDGET_KEYS = (
    "filter_date_range",
    "filter_city",
    "filter_customer",
    "filter_product",
)


def clear_sidebar_filters():
    for key in FILTER_WIDGET_KEYS:
        st.session_state.pop(key, None)


def apply_sidebar_filters(df):
    min_date = df["invoice_date"].dropna().min().date()
    max_date = df["invoice_date"].dropna().max().date()

    st.sidebar.markdown('<div class="sidebar-title">Filtreler</div>', unsafe_allow_html=True)
    st.sidebar.button(
        "Filtreleri Temizle",
        on_click=clear_sidebar_filters,
        use_container_width=True,
    )

    date_range = st.sidebar.date_input(
        "Tarih aralığı",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="filter_date_range",
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    elif isinstance(date_range, tuple):
        start_date = end_date = date_range[0] if date_range else min_date
    else:
        start_date = end_date = date_range

    def make_options(series: pd.Series):
        values = sorted(series.dropna().unique().tolist())
        return ["Hepsi"] + values if values else ["Hepsi"]

    df_date = sa.filter_data(df, start_date=start_date, end_date=end_date)
    city_options = make_options(df_date["city"]) if not df_date.empty else ["Hepsi"]
    city = st.sidebar.selectbox("İl", city_options, key="filter_city")

    df_city = df_date if city == "Hepsi" else df_date[df_date["city"] == city]
    customer_options = (
        make_options(df_city["customer_name"]) if not df_city.empty else ["Hepsi"]
    )
    customer = st.sidebar.selectbox(
        "Müşteri",
        customer_options,
        key="filter_customer",
    )

    df_customer = (
        df_city if customer == "Hepsi" else df_city[df_city["customer_name"] == customer]
    )
    product_options = (
        make_options(df_customer["product_name"])
        if not df_customer.empty
        else ["Hepsi"]
    )
    product = st.sidebar.selectbox("Ürün", product_options, key="filter_product")

    filtered_df = sa.filter_data(
        df,
        city=None if city == "Hepsi" else city,
        customer=None if customer == "Hepsi" else customer,
        product=None if product == "Hepsi" else product,
        start_date=start_date,
        end_date=end_date,
    )

    return filtered_df, {
        "start_date": start_date,
        "end_date": end_date,
        "city": city,
        "customer": customer,
        "product": product,
    }
