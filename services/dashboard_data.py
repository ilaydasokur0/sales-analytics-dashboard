import services.analysis as sa


def prepare_dashboard_data(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
    current_month_df,
    previous_month_df
):
    # Seçili filtre bir çeyrekse "Q", değilse (ay ya da "Hepsi") "M" bazında
    # karşılaştırma yapılır. current_period/previous_period zaten
    # get_month_comparison_frames tarafından bu freq ile üretilmiş olur.
    freq = "Q" if active_filters.get("period_type") == "quarter" else "M"
    selected_periods = active_filters.get("selected_periods") or None

    # Ulusal veriler
    national_df = sa.filter_data(
        sales_df,
        customer=None if active_filters["customer"] == "Hepsi" else active_filters["customer"],
        product=None if active_filters["product"] == "Hepsi" else active_filters["product"],
        start_date=active_filters["start_date"],
        end_date=active_filters["end_date"],
        periods=selected_periods,
        period_freq=freq,
    )

    national_summary_df = national_df.copy()

    if comparison_enabled:
        national_df = national_df[
            national_df["invoice_date"].dt.to_period(freq) == current_period
        ]

    national_previous_df = (
        national_summary_df[
            national_summary_df["invoice_date"].dt.to_period(freq) == previous_period
        ]
        if comparison_enabled and previous_period is not None
        else national_summary_df.iloc[0:0]
    )

    # İl + müşteri seçimi
    city_and_customer_selected = (
        active_filters["city"] != "Hepsi"
        and active_filters["customer"] != "Hepsi"
    )

    city_and_customer_and_product_selected = (
        active_filters["city"] != "Hepsi"
        and active_filters["customer"] != "Hepsi"
        and active_filters["product"] != "Hepsi"
    )

    # İl bazlı veriler
    city_base_df = sa.filter_data(
        sales_df,
        city=None if active_filters["city"] == "Hepsi" else active_filters["city"],
        product=None if active_filters["product"] == "Hepsi" else active_filters["product"],
        start_date=active_filters["start_date"],
        end_date=active_filters["end_date"],
        periods=selected_periods,
        period_freq=freq,
    )

    if comparison_enabled:
        city_base_df = city_base_df[
            city_base_df["invoice_date"].dt.to_period(freq) == current_period
        ]

    return (
        current_month_df,
        previous_month_df,
        national_df,
        national_summary_df,
        national_previous_df,
        city_base_df,
        city_and_customer_selected,
        city_and_customer_and_product_selected,
    )


def get_month_comparison_frames(df, filters):
    # Seçili filtre bir çeyrekse "Q" bazında, değilse (ay ya da "Hepsi")
    # "M" bazında en güncel dönemi ve bir önceki dönemi bulur.
    freq = "Q" if filters.get("period_type") == "quarter" else "M"
    selected_periods = filters.get("selected_periods") or []

    base_df = sa.filter_data(
        df,
        city=None if filters["city"] == "Hepsi" else filters["city"],
        customer=None if filters["customer"] == "Hepsi" else filters["customer"],
        product=None if filters["product"] == "Hepsi" else filters["product"],
    )

    # "Hepsi" (hiçbir ay/çeyrek seçili değil): tüm tarih aralığı, karşılaştırma yok.
    if filters.get("period_type") is None:
        selected_df = sa.filter_data(
            base_df,
            start_date=filters["start_date"],
            end_date=filters["end_date"],
        )
        return selected_df, selected_df.iloc[0:0], False, None, None

    # Birden fazla ay/çeyrek seçili: seçilenlerin TOPLAMI (birleşimi)
    # gösterilir, önceki döneme göre karşılaştırma kapatılır.
    if len(selected_periods) > 1:
        selected_df = sa.filter_data(base_df, periods=selected_periods, period_freq=freq)
        return selected_df, selected_df.iloc[0:0], False, None, None

    # Tek ay / tek çeyrek seçili: mevcut (önceki dönemle karşılaştırmalı) davranış.
    selected_df = sa.filter_data(base_df, periods=selected_periods, period_freq=freq)

    if selected_df.empty:
        return selected_df, selected_df, True, None, None

    latest_period = selected_df["invoice_date"].dt.to_period(freq).max()

    base_periods = base_df["invoice_date"].dt.to_period(freq)
    previous_candidates = base_periods[base_periods < latest_period]
    previous_period = (
        previous_candidates.max()
        if not previous_candidates.empty
        else None
    )

    current_df = selected_df[
        selected_df["invoice_date"].dt.to_period(freq) == latest_period
    ]

    previous_df = (
        base_df[base_periods == previous_period]
        if previous_period is not None
        else base_df.iloc[0:0]
    )

    return (
        current_df,
        previous_df,
        previous_period is not None,
        latest_period,
        previous_period,
    )