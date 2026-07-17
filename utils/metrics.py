import analysis as sa
def get_amount_share(df, group_col, value_col="total_amount"):
    grouped = df.groupby(group_col)[value_col].sum()
    total = grouped.sum()

    if total == 0:
        return grouped * 0

    return ((grouped / total) * 100).round(2)



def get_month_comparison_frames(df, filters):
    base_df = sa.filter_data(  #filtreler uygulanıyor
        df,
        city=None if filters["city"] == "Hepsi" else filters["city"],
        customer=None if filters["customer"] == "Hepsi" else filters["customer"],
        product=None if filters["product"] == "Hepsi" else filters["product"],
    )
    selected_df = sa.filter_data(
        base_df,  #base_df üzerine tarih filtresi ekleniyor
        start_date=filters["start_date"],
        end_date=filters["end_date"],
    )
    data_start = df["invoice_date"].min().date()
    data_end = df["invoice_date"].max().date()

    if filters["start_date"] == data_start and filters["end_date"] == data_end:
        return selected_df, selected_df.iloc[0:0], False, None, None

    if selected_df.empty:
        return selected_df, selected_df, True, None, None

    latest_period = selected_df["invoice_date"].dt.to_period("M").max()
    base_periods = base_df["invoice_date"].dt.to_period("M")
    previous_candidates = base_periods[base_periods < latest_period]
    previous_period = previous_candidates.max() if not previous_candidates.empty else None
    current_df = selected_df[selected_df["invoice_date"].dt.to_period("M") == latest_period]
    previous_df = (
        base_df[base_periods == previous_period]
        if previous_period is not None
        else base_df.iloc[0:0]
    )
    return current_df, previous_df, previous_period is not None, latest_period, previous_period


def get_city_share(national_df, city_df):
    """Return percentage share of city_df's total_amount over national_df's total_amount."""
    national_sales = sa.get_total_sales(national_df)
    city_sales = sa.get_total_sales(city_df)
    return 0 if national_sales == 0 else (city_sales / national_sales) * 100


def get_customer_city_share(city_base_df, customer_df):
    """Return percentage share of customer_df's total_amount over all customers in city_base_df."""
    city_sales_all_customers = sa.get_total_sales(city_base_df)
    customer_sales_in_city = sa.get_total_sales(customer_df)
    return 0 if city_sales_all_customers == 0 else (customer_sales_in_city / city_sales_all_customers) * 100