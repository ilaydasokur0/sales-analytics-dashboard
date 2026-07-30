import pandas as pd
import streamlit as st

from services import analysis as sa


FILTER_WIDGET_KEYS = ( 
    "filter_month",
    "filter_quarter",
    "filter_city",
    "filter_customer",
    "filter_product",
)

TURKISH_MONTH_ABBR = [
    "Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara",
]

QUARTER_LABELS = ["Q1", "Q2", "Q3", "Q4"]

MONTH_GRID_ROWS = 1
QUARTER_GRID_ROWS = 1


def clear_sidebar_filters():
    for key in FILTER_WIDGET_KEYS:
        st.session_state.pop(key, None)


def _validated_select(label, options, key):
    if st.session_state.get(key) not in options:
        st.session_state[key] = "Hepsi"
    return st.sidebar.selectbox(label, options, key=key)


def _render_month_grid(month_periods):
    period_keys = [str(p) for p in month_periods]

    if st.session_state.get("filter_month") not in period_keys:
        st.session_state["filter_month"] = ""

    selected_key = st.session_state["filter_month"]

    st.sidebar.markdown('<div class="mini-section-title">Ay</div>', unsafe_allow_html=True)

    with st.sidebar.container(key="month_grid"):
        for row_start in range(0, len(month_periods), MONTH_GRID_ROWS):
            row = list(zip(period_keys, month_periods))[row_start:row_start + MONTH_GRID_ROWS]
            cols = st.columns(MONTH_GRID_ROWS, gap="small")
            for col, (period_key, period) in zip(cols, row):
                is_selected = period_key == selected_key
                clicked = col.button(
                    TURKISH_MONTH_ABBR[period.month - 1],
                    key=f"month_btn_{period_key}",
                    type="primary" if is_selected else "secondary",
                    use_container_width=True,
                )
                if clicked:
                    # Seçili olan aya tekrar basılırsa filtreyi kaldır, değilse yeni ayı atayıp sayfayı yenile
                    if is_selected:
                        st.session_state["filter_month"] = ""
                    else:
                        st.session_state["filter_month"] = period_key
                        st.session_state["filter_quarter"] = ""  # dışlayıcı: ay seçilince çeyrek temizlenir
                    st.rerun()

    selected_key = st.session_state["filter_month"]
    if not selected_key:
        return None
    return pd.Period(selected_key, freq="M")


def _render_quarter_grid(quarter_periods):
    period_keys = [str(p) for p in quarter_periods]

    if st.session_state.get("filter_quarter") not in period_keys:
        st.session_state["filter_quarter"] = ""

    selected_key = st.session_state["filter_quarter"]

    st.sidebar.markdown('<div class="mini-section-title">Çeyrek</div>', unsafe_allow_html=True)

    with st.sidebar.container(key="quarter_grid"):
        # Ay grid'iyle aynı DOM yapısını kurmak için her buton ayrı bir st.columns(1) satırı olarak üretiliyor
        for row_start in range(0, len(quarter_periods), QUARTER_GRID_ROWS):
            row = list(zip(period_keys, quarter_periods))[row_start:row_start + QUARTER_GRID_ROWS]
            cols = st.columns(QUARTER_GRID_ROWS, gap="small")
            for col, (period_key, period) in zip(cols, row):
                is_selected = period_key == selected_key
                clicked = col.button(
                    QUARTER_LABELS[period.quarter - 1],
                    key=f"quarter_btn_{period_key}",
                    type="primary" if is_selected else "secondary",
                    use_container_width=True,
                )
                if clicked:
                    # Seçili olan çeyreğe tekrar basılırsa filtreyi kaldır, değilse yeni çeyreği atayıp ayı temizle
                    if is_selected:
                        st.session_state["filter_quarter"] = ""
                    else:
                        st.session_state["filter_quarter"] = period_key
                        st.session_state["filter_month"] = ""  # dışlayıcı: çeyrek seçilince ay temizlenir
                    st.rerun()

    selected_key = st.session_state["filter_quarter"]
    if not selected_key:
        return None
    return pd.Period(selected_key, freq="Q")


def _render_filter_summary(city, customer, product, start_date, end_date):

    summary_parts = [f"Seçili Filtreler - Tarih: {start_date} - {end_date}"]
    if city != "Hepsi":
        summary_parts.append(f"İl: {city}")
    if customer != "Hepsi":
        summary_parts.append(f"Müşteri: {customer}")
    if product != "Hepsi":
        summary_parts.append(f"Ürün: {product}")

    st.sidebar.markdown(
        f'<div class="sidebar-filter-summary">{" | ".join(summary_parts)}</div>',
        unsafe_allow_html=True,
    )


def _render_comparison_status(selected_month_period, selected_quarter_period, month_periods, quarter_periods):
    if selected_quarter_period is not None:
        previous_period = selected_quarter_period - 1
        if str(previous_period) in {str(period) for period in quarter_periods}:
            message = f"Karşılaştırma: {previous_period} / {selected_quarter_period}"
        else:
            message = "Seçilen çeyrek için karşılaştırma yapılamıyor."
    elif selected_month_period is not None:
        previous_period = selected_month_period - 1
        if str(previous_period) in {str(period) for period in month_periods}:
            message = f"Karşılaştırma: {previous_period} / {selected_month_period}"
        else:
            message = "Seçilen ay için karşılaştırma yapılamıyor."
    else:
        return

    st.sidebar.markdown(
        f'<div class="sidebar-comparison-status">{message}</div>',
        unsafe_allow_html=True,
    )


def apply_sidebar_filters(df):
    min_date = df["invoice_date"].dropna().min().date()
    max_date = df["invoice_date"].dropna().max().date()

    st.sidebar.markdown(
        '<div class="sidebar-title">Satış Analiz Dashboard</div>',
        unsafe_allow_html=True,
    )
    st.sidebar.markdown('<div class="sidebar-filter-heading">Filtreler</div>', unsafe_allow_html=True)
    st.sidebar.button(
        "Filtreleri Temizle",
        on_click=clear_sidebar_filters,
        use_container_width=True,
    )

    month_periods = list(pd.period_range(start=min_date, end=max_date, freq="M"))
    quarter_periods = list(pd.period_range(start=min_date, end=max_date, freq="Q"))

    selected_month_period = _render_month_grid(month_periods)
    selected_quarter_period = _render_quarter_grid(quarter_periods)
    _render_comparison_status(selected_month_period, selected_quarter_period, month_periods, quarter_periods)

    if selected_quarter_period is not None:
        period_type = "quarter"
        start_date = selected_quarter_period.start_time.date()
        end_date = min(selected_quarter_period.end_time.date(), max_date)

        prev_period = selected_quarter_period - 1
        prev_start_date = prev_period.start_time.date()
        prev_end_date = prev_period.end_time.date()
        comparison_available = str(prev_period) in [str(p) for p in quarter_periods]
        month_label = "Hepsi"
        quarter_label = f"{QUARTER_LABELS[selected_quarter_period.quarter - 1]} {selected_quarter_period.year}"
    elif selected_month_period is not None:
        period_type = "month"
        start_date = selected_month_period.start_time.date()
        end_date = min(selected_month_period.end_time.date(), max_date)

        prev_period = selected_month_period - 1
        prev_start_date = prev_period.start_time.date()
        prev_end_date = prev_period.end_time.date()
        comparison_available = str(prev_period) in [str(p) for p in month_periods]
        month_label = TURKISH_MONTH_ABBR[selected_month_period.month - 1]
        quarter_label = "Hepsi"
    else:
        period_type = None
        start_date = min_date
        end_date = max_date
        prev_start_date = min_date
        prev_end_date = max_date
        comparison_available = False
        month_label = "Hepsi"
        quarter_label = "Hepsi"

    def make_options(series: pd.Series):
        values = sorted(series.dropna().unique().tolist())
        return ["Hepsi"] + values if values else ["Hepsi"]

    city_options = make_options(df["city"])
    city = _validated_select("İl", city_options, "filter_city")

    df_city = df if city == "Hepsi" else df[df["city"] == city]
    customer_options = (
        make_options(df_city["customer_name"]) if not df_city.empty else ["Hepsi"]
    )
    customer = _validated_select("Müşteri", customer_options, "filter_customer")

    df_customer = (
        df_city if customer == "Hepsi" else df_city[df_city["customer_name"] == customer]
    )
    product_options = (
        make_options(df_customer["product_name"])
        if not df_customer.empty
        else ["Hepsi"]
    )
    product = _validated_select("Ürün", product_options, "filter_product")

    _render_filter_summary(city, customer, product, start_date, end_date)

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
        "quarter_label": quarter_label,
        "period_type": period_type,
        "city": city,
        "customer": customer,
        "product": product,
    }