from services.formatters import format_currency
from services import analysis as sa
def build_ranked_table(
    current_df,        # Bu aya ait filtrelenmiş veriler
    previous_df,       # Önceki aya ait filtrelenmiş veriler
    group_col,         
    value_col,         
    *,
    top_n=3,           
    ascending=False,   
    group_label=None,  
    value_label=None,  
    currency=False,    
):
    current_totals = current_df.groupby(group_col)[value_col].sum() # Aynı müşteri/ürün/ili bir araya getirip toplam değeri hesaplıyoruz.
    previous_totals = previous_df.groupby(group_col)[value_col].sum()

    comparison = current_totals.to_frame("current").join(
        previous_totals.rename("previous"), how="outer"
    ).fillna(0) #iki tabloyu birleştirip, eksik değerleri 0 ile dolduruyoruz

    table = (
        comparison[["current"]]
        .sort_values("current", ascending=ascending)
        .head(top_n)
        .reset_index()
    ) #birleştirilen tablodan sadece current değerlerini alıp, sıralayıp, top_n kadarını alıyoruz.

    table.columns = [group_label or group_col, value_label or value_col]

    def format_change(current_value, previous_value):
        if previous_value == 0:
            if current_value == 0:
                return ""
            return "▲"

        change_ratio = ((current_value - previous_value) / previous_value) * 100
        return "▲" if change_ratio >= 0 else "▼"

    formatted_values = []

    for item in table[group_label or group_col]:
        current_value = current_totals.get(item, 0)
        previous_value = previous_totals.get(item, 0)

        display_value = format_currency(current_value) if currency else current_value
        if previous_df.empty:
            formatted_values.append(str(display_value))
            continue
        formatted_values.append(f"{display_value} {format_change(current_value, previous_value)}")

    table[value_label or value_col] = formatted_values

    return table

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

    if total_sales == 0:
        table["share"] = 0.0
    else:
        table["share"] = (table["total_amount"] / total_sales * 100).round(1)

    return table