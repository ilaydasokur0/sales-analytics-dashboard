import streamlit as st
import analysis as sa

def apply_sidebar_filters(df):
    min_date = df["invoice_date"].dropna().min().date()
    max_date = df["invoice_date"].dropna().max().date()

    def select_option(label, values):
        options = ["Hepsi"] + sorted(values.dropna().unique().tolist())
        return st.sidebar.selectbox(label, options)

    st.sidebar.markdown('<div class="sidebar-title">Filtreler</div>', unsafe_allow_html=True)
    st.sidebar.caption("Boş bırakmak için Hepsi seç.")

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

    city = select_option("İl", df["city"])
    customer = select_option("Müşteri", df["customer_name"])
    product = select_option("Ürün", df["product_name"])

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