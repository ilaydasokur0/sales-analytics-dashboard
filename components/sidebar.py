import streamlit as st
from services import analysis as sa
import pandas as pd


def apply_sidebar_filters(df):
    
    min_date = df["invoice_date"].dropna().min().date()
    max_date = df["invoice_date"].dropna().max().date()

    st.sidebar.markdown('<div class="sidebar-title">Filtreler</div>', unsafe_allow_html=True)

    # Date range first (controls available rows for subsequent dropdowns)
    date_range = st.sidebar.date_input(
        "Tarih aralığı",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date = date_range[0]
        end_date = date_range[1]
    elif isinstance(date_range, tuple):
        start_date = end_date = date_range[0] if date_range else min_date
    else:
        start_date = end_date = date_range

    # Helper to build options list (always include 'Hepsi')
    def make_options(series: pd.Series):
        vals = series.dropna().unique().tolist()
        vals = sorted(vals)
        return ["Hepsi"] + vals if vals else ["Hepsi"]

    # Base df filtered by date only
    df_date = sa.filter_data(df, start_date=start_date, end_date=end_date)

    # City options depend on date range
    city_options = make_options(df_date["city"]) if not df_date.empty else ["Hepsi"]
    city = st.sidebar.selectbox("İl", city_options)

    # If a specific city is selected, filter by it for downstream options
    if city == "Hepsi":
        df_city = df_date
    else:
        df_city = df_date[df_date["city"] == city]

    # Customer options depend on date range and (optional) city
    customer_options = make_options(df_city["customer_name"]) if not df_city.empty else ["Hepsi"]
    customer = st.sidebar.selectbox("Müşteri", customer_options)

    # If a specific customer is selected, filter by it for downstream options
    if customer == "Hepsi":
        df_customer = df_city
    else:
        df_customer = df_city[df_city["customer_name"] == customer]

    # Product options depend on date range + city + customer (respecting Hepsi semantics)
    product_options = make_options(df_customer["product_name"]) if not df_customer.empty else ["Hepsi"]
    product = st.sidebar.selectbox("Ürün", product_options)

    # Final filtered dataframe - same logic as before (use sa.filter_data)
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