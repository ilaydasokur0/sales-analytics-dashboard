import pandas as pd
import streamlit as st

from services import analysis as sa


FILTER_WIDGET_KEYS = (
    "filter_months",
    "filter_quarters",
    "filter_city",
    "filter_customer",
    "filter_product",
)

TURKISH_MONTH_ABBR = [
    "Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara",
]

QUARTER_LABELS = ["Ç1", "Ç2", "Ç3", "Ç4"]

MONTH_GRID_ROWS = 1


def clear_sidebar_filters():
    for key in FILTER_WIDGET_KEYS:
        st.session_state.pop(key, None)


def _validated_select(label, options, key):
    if st.session_state.get(key) not in options:
        st.session_state[key] = "Hepsi"
    return st.sidebar.selectbox(label, options, key=key)


def _render_month_grid(month_periods):
    """Ay butonları: çoklu seçime izin verir (bir aya tekrar basılırsa o ay
    kaldırılır). Bir ay seçildiğinde çeyrek seçimleri dışlayıcı olarak
    temizlenir. DOM yapısı (her buton kendi tek-sütunlu satırında) CSS
    grid'in 4'lü düzeni doğru şekilde oluşturabilmesi için bilinçli olarak
    korunmuştur — bunu değiştirmeyin."""

    period_keys = [str(p) for p in month_periods]

    valid_selected = [k for k in st.session_state.get("filter_months", []) if k in period_keys]
    st.session_state["filter_months"] = valid_selected
    selected_keys = set(valid_selected)

    st.sidebar.markdown('<div class="mini-section-title">Ay</div>', unsafe_allow_html=True)

    with st.sidebar.container(key="month_grid"):
        for row_start in range(0, len(month_periods), MONTH_GRID_ROWS):
            row = list(zip(period_keys, month_periods))[row_start:row_start + MONTH_GRID_ROWS]
            cols = st.columns(MONTH_GRID_ROWS, gap="small")
            for col, (period_key, period) in zip(cols, row):
                is_selected = period_key in selected_keys
                clicked = col.button(
                    TURKISH_MONTH_ABBR[period.month - 1],
                    key=f"month_btn_{period_key}",
                    type="primary" if is_selected else "secondary",
                    use_container_width=True,
                )
                if clicked:
                    current = set(st.session_state.get("filter_months", []))
                    if period_key in current:
                        current.discard(period_key)
                    else:
                        current.add(period_key)
                        st.session_state["filter_quarters"] = []  # dışlayıcı: ay seçilince çeyrekler temizlenir
                    st.session_state["filter_months"] = sorted(current)
                    st.rerun()

    selected = sorted(st.session_state.get("filter_months", []))
    return [pd.Period(k, freq="M") for k in selected]


def _render_quarter_grid(quarter_periods):
    """Çeyrek butonları: ay grid'iyle birebir aynı tasarım/DOM yapısı,
    çoklu seçime izin verir, seçilince ay filtrelerini dışlayıcı olarak
    temizler."""

    period_keys = [str(p) for p in quarter_periods]

    valid_selected = [k for k in st.session_state.get("filter_quarters", []) if k in period_keys]
    st.session_state["filter_quarters"] = valid_selected
    selected_keys = set(valid_selected)

    st.sidebar.markdown('<div class="mini-section-title">Çeyrek</div>', unsafe_allow_html=True)

    with st.sidebar.container(key="quarter_grid"):
        for row_start in range(0, len(quarter_periods), 1):
            row = list(zip(period_keys, quarter_periods))[row_start:row_start + 1]
            cols = st.columns(1, gap="small")
            for col, (period_key, period) in zip(cols, row):
                is_selected = period_key in selected_keys
                clicked = col.button(
                    QUARTER_LABELS[period.quarter - 1],
                    key=f"quarter_btn_{period_key}",
                    type="primary" if is_selected else "secondary",
                    use_container_width=True,
                )
                if clicked:
                    current = set(st.session_state.get("filter_quarters", []))
                    if period_key in current:
                        current.discard(period_key)
                    else:
                        current.add(period_key)
                        st.session_state["filter_months"] = []  # dışlayıcı: çeyrek seçilince aylar temizlenir
                    st.session_state["filter_quarters"] = sorted(current)
                    st.rerun()

    selected = sorted(st.session_state.get("filter_quarters", []))
    return [pd.Period(k, freq="Q") for k in selected]


def _render_filter_summary(city, customer, product, start_date, end_date, selected_periods, period_type):

    if selected_periods:
        if period_type == "quarter":
            labels = [
                f"{QUARTER_LABELS[pd.Period(p, freq='Q').quarter - 1]} {pd.Period(p, freq='Q').year}"
                for p in selected_periods
            ]
        else:
            labels = [
                f"{TURKISH_MONTH_ABBR[pd.Period(p, freq='M').month - 1]} {pd.Period(p, freq='M').year}"
                for p in selected_periods
            ]
        date_part = f"Dönem: {', '.join(labels)}"
    else:
        date_part = f"Tarih: {start_date} - {end_date}"

    summary_parts = [f"Seçili Filtreler - {date_part}"]
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


def _render_comparison_status(selected_months, selected_quarters, month_periods, quarter_periods):
    # Çoklu seçimde karşılaştırma zaten kapalı; ekstra bir durum mesajı gösterilmez.
    if selected_quarters:
        if len(selected_quarters) > 1:
            return
        selected = selected_quarters[0]
        previous_period = selected - 1
        if str(previous_period) in {str(p) for p in quarter_periods}:
            message = f"Karşılaştırma: {previous_period} / {selected}"
        else:
            message = "Seçilen çeyrek için karşılaştırma yapılamıyor."
    elif selected_months:
        if len(selected_months) > 1:
            return
        selected = selected_months[0]
        previous_period = selected - 1
        if str(previous_period) in {str(p) for p in month_periods}:
            message = f"Karşılaştırma: {previous_period} / {selected}"
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

    selected_months = _render_month_grid(month_periods)
    selected_quarters = _render_quarter_grid(quarter_periods)
    _render_comparison_status(selected_months, selected_quarters, month_periods, quarter_periods)

    if selected_quarters:
        period_type = "quarter"
        active_periods = sorted(selected_quarters)
        selected_periods = [str(p) for p in active_periods]
        start_date = min(p.start_time.date() for p in active_periods)
        end_date = min(max(p.end_time.date() for p in active_periods), max_date)

        if len(active_periods) == 1:
            prev_period = active_periods[0] - 1
            prev_start_date = prev_period.start_time.date()
            prev_end_date = prev_period.end_time.date()
            comparison_available = str(prev_period) in [str(p) for p in quarter_periods]
            quarter_label = f"{QUARTER_LABELS[active_periods[0].quarter - 1]} {active_periods[0].year}"
        else:
            prev_start_date = None
            prev_end_date = None
            comparison_available = False
            quarter_label = f"{len(active_periods)} Çeyrek Seçili"

        # month_label bilinçli olarak "Hepsi" bırakılıyor: aylık performans
        # grafiğindeki "tek ay vurgusu" (bar chart) mantığı sadece tek ay
        # seçiliyken devreye girer, çeyrekte grafik normal görünümde kalır.
        month_label = "Hepsi"

    elif selected_months:
        period_type = "month"
        active_periods = sorted(selected_months)
        selected_periods = [str(p) for p in active_periods]
        start_date = min(p.start_time.date() for p in active_periods)
        end_date = min(max(p.end_time.date() for p in active_periods), max_date)

        if len(active_periods) == 1:
            prev_period = active_periods[0] - 1
            prev_start_date = prev_period.start_time.date()
            prev_end_date = prev_period.end_time.date()
            comparison_available = str(prev_period) in [str(p) for p in month_periods]
            month_label = TURKISH_MONTH_ABBR[active_periods[0].month - 1]
        else:
            prev_start_date = None
            prev_end_date = None
            comparison_available = False
            month_label = "Hepsi"

        quarter_label = "Hepsi"

    else:
        period_type = None
        selected_periods = []
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

    _render_filter_summary(city, customer, product, start_date, end_date, selected_periods, period_type)

    filtered_df = sa.filter_data(
        df,
        city=None if city == "Hepsi" else city,
        customer=None if customer == "Hepsi" else customer,
        product=None if product == "Hepsi" else product,
        start_date=start_date,
        end_date=end_date,
        periods=selected_periods if selected_periods else None,
        period_freq="Q" if period_type == "quarter" else "M",
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
        "selected_periods": selected_periods,
        "city": city,
        "customer": customer,
        "product": product,
    }