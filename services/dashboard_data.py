import analysis as sa
from utils.metrics import get_month_comparison_frames 

def prepare_dashboard_data(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
):
    # Karşılaştırma için geçerli ay ve önceki ay verileri
    (
        current_month_df,
        previous_month_df,
        comparison_enabled_local,
        current_period_local,
        previous_period_local,
    ) = get_month_comparison_frames(sales_df, active_filters)

    # Ulusal veriler
    national_df = sa.filter_data(
        sales_df,
        customer=None if active_filters["customer"] == "Hepsi" else active_filters["customer"],
        product=None if active_filters["product"] == "Hepsi" else active_filters["product"],
        start_date=active_filters["start_date"],
        end_date=active_filters["end_date"],
    )

    national_summary_df = national_df.copy()

    if comparison_enabled:
        national_df = national_df[
            national_df["invoice_date"].dt.to_period("M") == current_period
        ]

    national_previous_df = (
        national_summary_df[
            national_summary_df["invoice_date"].dt.to_period("M") == previous_period
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
    )

    if comparison_enabled:
        city_base_df = city_base_df[
            city_base_df["invoice_date"].dt.to_period("M") == current_period
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