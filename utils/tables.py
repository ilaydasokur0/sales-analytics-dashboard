from services import analysis as sa
from services.formatters import format_currency


def build_ranked_table(
    current_df,
    group_col,
    value_col,
    *,
    top_n=None,
    ascending=False,
    group_label=None,
    value_label=None,
):
    """Prepare a numeric ranking DataFrame for a chart component."""
    table = (
        current_df.groupby(group_col, as_index=False)[value_col]
        .sum()
        .sort_values(value_col, ascending=ascending)
        .rename(
            columns={
                group_col: group_label or group_col,
                value_col: value_label or value_col,
            }
        )
        .reset_index(drop=True)
    )

    return table if top_n is None else table.head(top_n)


def build_change_table(
    current_df,
    previous_df,
    group_col,
    value_col,
    *,
    top_n=3,
    group_label=None,
    value_label=None,
    currency=False,
):
    current_totals = current_df.groupby(group_col)[value_col].sum()
    previous_totals = previous_df.groupby(group_col)[value_col].sum()
    show_change = not previous_df.empty
    comparison = current_totals.to_frame("current").join(
        previous_totals.rename("previous"), how="outer"
    ).fillna(0)
    comparison["change"] = comparison["current"] - comparison["previous"]
    table = comparison.sort_values("change").head(top_n).reset_index()
    table.columns = [group_label or group_col, "current", "previous", "change"]

    def format_change(current_value, previous_value):
        if not show_change:
            return ""
        if previous_value == 0:
            return "▲" if current_value else ""
        change_ratio = ((current_value - previous_value) / previous_value) * 100
        return "▲" if change_ratio >= 0 else "▼"

    display_values = []
    for _, row in table.iterrows():
        value = format_currency(row["current"]) if currency else f"{row['current']:,.0f}"
        display_values.append(f"{value} {format_change(row['current'], row['previous'])}")

    return table[[group_label or group_col]].assign(
        **{value_label or value_col: display_values}
    )


def build_customer_revenue_share_table(current_df, top_n=10):
    customer_sales = sa.get_customer_sales(current_df)

    if customer_sales.empty:
        return customer_sales.reset_index()

    total_sales = customer_sales.sum()
    table = (
        customer_sales
        .reset_index()
        .sort_values("total_amount", ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )
    table["share"] = 0.0 if total_sales == 0 else (table["total_amount"] / total_sales * 100).round(1)

    return table

def build_product_revenue_share_table(current_df, top_n=10):
    product_sales = sa.get_product_sales(current_df)

    if product_sales.empty:
        return product_sales.reset_index()

    total_sales = product_sales.sum()
    table = (
        product_sales
        .reset_index()
        .sort_values("total_amount", ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )
    table["share"] = 0.0 if total_sales == 0 else (table["total_amount"] / total_sales * 100).round(1)

    return table
