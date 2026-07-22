import streamlit as st
from components import charts
from services import analysis as sa
import html
from components.kpi import get_trend_arrow
from utils.tables import build_ranked_table, build_change_table
from utils.tables import build_customer_revenue_share_table

def render_customer_revenue_share_chart(current_df):
    chart_df = build_customer_revenue_share_table(current_df)

    charts.render_horizontal_bar_chart(
        title="Müşteri Ciro Payları",
        chart_df=chart_df,
        label_col="customer_name",
        value_col="share",
        value_suffix="%"
    )

def render_city_summary_cards(
    city,
    current_df,
    previous_df,
    national_current_df,
    national_previous_df,
    comparison_enabled,
):
    city_sales_current = (
        national_current_df.groupby("city")["total_amount"].sum().sort_values(ascending=False)
    )
    total_city_count = len(city_sales_current)
    city_rank_current = (
        city_sales_current.index.get_loc(city) + 1
        if city in city_sales_current.index
        else total_city_count
    )

    rank_arrow = ""
    if comparison_enabled and not national_previous_df.empty:
        city_sales_previous = (
            national_previous_df.groupby("city")["total_amount"].sum().sort_values(ascending=False)
        )
        if city in city_sales_previous.index:
            city_rank_previous = city_sales_previous.index.get_loc(city) + 1
            if city_rank_current < city_rank_previous:
                rank_arrow = "▲"
            elif city_rank_current > city_rank_previous:
                rank_arrow = "▼"

    variety_current = current_df["product_id"].nunique()
    variety_previous = previous_df["product_id"].nunique() if not previous_df.empty else None
    variety_arrow = get_trend_arrow(variety_current, variety_previous, comparison_enabled)

    city_total = sa.get_total_sales(current_df)
    if city_total == 0 or current_df.empty:
        top_customer_name = "-"
        top_customer_share = 0
    else:
        customer_sales = (
            current_df.groupby("customer_name")["total_amount"].sum().sort_values(ascending=False)
        )
        top_customer_name = customer_sales.index[0]
        top_customer_share = (customer_sales.iloc[0] / city_total) * 100

    st.subheader("İl Kartları")
    st.caption(" ")
    st.markdown(
        f"""
        <div class="city-summary-stack">
            <div class="city-summary-card">
                <div class="city-summary-label">Ulusal Ciro Sırası</div>
                <div class="city-summary-value">{city_rank_current} / {total_city_count} {rank_arrow}</div>
            </div>
            <div class="city-summary-card">
                <div class="city-summary-label">Ürün Çeşitliliği</div>
                <div class="city-summary-value">{variety_current} ürün {variety_arrow}</div>
            </div>
            <div class="city-summary-card">
                <div class="city-summary-label">En Büyük Müşteri</div>
                <div class="city-summary-value">{top_customer_name} (%{top_customer_share:.0f})</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_city_product_tables(current_df, previous_df):
    top_products = build_ranked_table(
        current_df,
        "product_name",
        "quantity",
        top_n=100,
        ascending=False,
        group_label="Ürün",
        value_label="Satış Adedi",
    )
    declining_products = build_change_table(
        current_df,
        previous_df,
        "product_name",
        "quantity",
        top_n=5,
        group_label="Ürün",
        value_label="Satış Adedi",
    )

    st.subheader("Ürün Performansı")
    st.caption("En Çok Satılan 5 Ürün")
    st.dataframe(top_products, hide_index=True, width="stretch", height=180)
    st.caption("En Çok Düşüş Yaşayan 5 Ürün")
    st.dataframe(declining_products, hide_index=True, width="stretch", height=180)


def render_city_customer_product_ranking(current_df):
    chart_df = build_ranked_table(
        current_df,
        "product_name",
        "quantity",
        group_label="Ürün",
        value_label="Satış Adedi",
    )

    with st.container(height=320):
        charts.render_horizontal_bar_chart(
            title="Ürün Sıralaması",
            chart_df=chart_df,
            label_col="Ürün",
            value_col="Satış Adedi",
        )

