from services.formatters import format_currency
import streamlit as st


def build_product_invoice_table(current_df):
    table = (
        current_df[
            [
                "invoice_id",
                "invoice_date",
                "quantity",
                "unit_price",
                "total_amount",
            ]
        ]
        .copy()
        .sort_values("invoice_date", ascending=False)
    )

    table = table.rename(
        columns={
            "invoice_id": "Fatura No",
            "invoice_date": "Fatura Tarihi",
            "quantity": "Satış Adedi",
            "unit_price": "Birim Fiyat",
            "total_amount": "Ciro",
        }
    )

    table["Fatura Tarihi"] = table["Fatura Tarihi"].dt.strftime("%d.%m.%Y")
    table["Birim Fiyat"] = table["Birim Fiyat"].apply(format_currency)
    table["Ciro"] = table["Ciro"].apply(format_currency)

    return table

def render_product_detail_table(current_df):
    st.subheader("Fatura Geçmişi")

    table = build_product_invoice_table(current_df)

    st.dataframe(
        table,
        hide_index=True,
        use_container_width=True,
        height=350,
    )