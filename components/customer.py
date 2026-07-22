import streamlit as st
from services.formatters import format_currency


def build_customer_product_summary(current_df, previous_df):
    current_totals = current_df.groupby("product_name").agg(
        quantity=("quantity", "sum"),
        amount=("total_amount", "sum"),
    )
    previous_totals = previous_df.groupby("product_name").agg(
        quantity=("quantity", "sum"),
        amount=("total_amount", "sum"),
    )

    comparison = current_totals.join(
        previous_totals, how="left", rsuffix="_previous"
    ).fillna(0)

    comparison = comparison.sort_values("amount", ascending=False).reset_index()

    def arrow(current_value, previous_value):
        if previous_df.empty:
            return ""
        if previous_value == 0:
            return "▲" if current_value else ""
        change_ratio = ((current_value - previous_value) / previous_value) * 100
        return "▲" if change_ratio >= 0 else "▼"

    comparison["Satış Adedi"] = comparison.apply(
        lambda row: f"{row['quantity']:,.0f} {arrow(row['quantity'], row['quantity_previous'])}".strip(),
        axis=1,
    )
    comparison["Ciro"] = comparison.apply(
        lambda row: f"{format_currency(row['amount'])} {arrow(row['amount'], row['amount_previous'])}".strip(),
        axis=1,
    )

    comparison = comparison.rename(columns={"product_name": "Ürün"})

    return comparison[["Ürün", "Satış Adedi", "Ciro"]]


def render_customer_detail_table(current_df, previous_df):
    # Wrapper to render customer-level product summary
    table = build_customer_product_summary(current_df, previous_df)
    st.subheader("Müşteri Ürünleri")
    st.dataframe(table, hide_index=True, width="stretch", height=420)

