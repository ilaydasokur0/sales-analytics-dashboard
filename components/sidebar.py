import pandas as pd
import streamlit as st

from services import analysis as sa


FILTER_WIDGET_KEYS = (
    "filter_month",
    "filter_city",
    "filter_customer",
    "filter_product",
)

TURKISH_MONTH_ABBR = [
    "Oca", "Şub", "Mar", "Nis", "May", "Haz",
    "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara",
]

MONTH_GRID_COLS = 4


def clear_sidebar_filters():
    for key in FILTER_WIDGET_KEYS:
        st.session_state.pop(key, None)


def _render_month_grid(month_periods):
    """Ayları 4'lü satırlar halinde buton grid'i olarak çizer.
    Seçili ay filtre kaldırılana kadar mavi (primary) kalır.
    Hiçbir ay seçilmemişse (ör. filtreler temizlendiğinde) genel
    toplam veriler gösterilir."""
    period_keys = [str(p) for p in month_periods]

    if st.session_state.get("filter_month") not in period_keys:
        st.session_state["filter_month"] = ""

    selected_key = st.session_state["filter_month"]

    st.sidebar.markdown('<div class="mini-section-title">Ay</div>', unsafe_allow_html=True)

    with st.sidebar.container(key="month_grid"):
        for row_start in range(0, len(month_periods), MONTH_GRID_COLS):
            row = list(zip(period_keys, month_periods))[row_start:row_start + MONTH_GRID_COLS]
            cols = st.columns(MONTH_GRID_COLS, gap="small")
            for col, (period_key, period) in zip(cols, row):
                is_selected = period_key == selected_key
                clicked = col.button(
                    TURKISH_MONTH_ABBR[period.month - 1],
                    key=f"month_btn_{period_key}",
                    type="primary" if is_selected else "secondary",
                    use_container_width=True,
                )
                if clicked and not is_selected:
                    st.session_state["filter_month"] = period_key
                    st.rerun()

    selected_key = st.session_state["filter_month"]
    if not selected_key:
        return None
    return pd.Period(selected_key, freq="M")


def apply_sidebar_filters(df):
    min_date = df["invoice_date"].dropna().min().date()
    max_date = df["invoice_date"].dropna().max().date()

    st.sidebar.markdown('<div class="sidebar-title">Filtreler</div>', unsafe_allow_html=True)
    st.sidebar.button(
        "Filtreleri Temizle",
        on_click=clear_sidebar_filters,
        use_container_width=True,
    )

    month_periods = list(pd.period_range(start=min_date, end=max_date, freq="M"))
    selected_period = _render_month_grid(month_periods)

    if selected_period is None:
        start_date = min_date
        end_date = max_date
        prev_start_date = None
        prev_end_date = None
        comparison_available = False
        month_label = "Hepsi"
    else:
        start_date = selected_period.start_time.date()
        end_date = min(selected_period.end_time.date(), max_date)

        prev_period = selected_period - 1
        prev_start_date = prev_period.start_time.date()
        prev_end_date = prev_period.end_time.date()
        comparison_available = str(prev_period) in [str(p) for p in month_periods]
        month_label = TURKISH_MONTH_ABBR[selected_period.month - 1]

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
        "prev_start_date": prev_start_date,
        "prev_end_date": prev_end_date,
        "comparison_available": comparison_available,
        "month_label": month_label,
        "city": city,
        "customer": customer,
        "product": product,
    }