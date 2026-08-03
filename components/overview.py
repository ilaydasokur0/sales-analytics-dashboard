import streamlit as st
from components.charts import (
    render_chart_controls,
    render_donut_chart,
    render_horizontal_bar_chart,
    render_monthly_chart_card,
    render_gauge_pair,
)
from components.city import render_city_summary_rank
from components.customer import render_customer_invoice_summary
from components.product import render_product_summary_rank
from services.analysis import get_amount_share
from utils.tables import (
    build_city_summary_rank,
    build_customer_invoice_summary,
    build_product_revenue_share_table,
    build_product_summary_rank,
    build_ranked_table,
)

def render_header(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
    current_month_df,
):
    if current_month_df.empty:
        st.warning("Seçilen filtrelerde veri bulunamadı. Filtreleri genişletip tekrar deneyin.")
        st.stop()

    st.markdown(
    """
    <div class="header-title-container">
        <div class="header-icon-box">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path d="M0 0h512v512H0z" fill="none" />
                <path fill="#0A2B47" d="M458.4 274.8c-11.9-67.2-40.9-118.3-64.9-114c-6.4 1.1-11.8 6.2-16 14.1c-1.9-2.7-3.8-5.4-5.8-7.9c5.1-13.5 8-28.1 8-43.4C379.6 55.3 324.3 0 256 0S132.4 55.3 132.4 123.6c0 15.3 2.9 29.9 8 43.4c-2 2.6-3.9 5.2-5.8 7.9c-4.2-7.9-9.6-13-16-14.1c-24-4.2-53.1 46.8-64.9 114c-11.9 67.2-2 125.1 22 129.4c11.2 2 23.5-8.2 34.7-26.4c24.5 68.6 80.5 116.6 145.7 116.6s121.1-48 145.7-116.6c11.2 18.2 23.5 28.4 34.7 26.4c23.9-4.2 33.7-62.2 21.9-129.4" />
                <path fill="#F4F9FC" d="M361.9 335.4c0 78-47.4 141.2-105.9 141.2s-105.9-63.2-105.9-141.2c0-43.6 14.9-82.6 38.2-108.6c19.5 12.8 42.7 20.3 67.7 20.3s48.3-7.5 67.7-20.3c23.4 26 38.2 65 38.2 108.6M167.7 141.2c0-43.9 39.5-79.4 88.3-79.4s88.3 35.6 88.3 79.4s-39.5 79.4-88.3 79.4s-88.3-35.5-88.3-79.4m110.4-35.3c0 12.2 9.9 22.1 22.1 22.1s22.1-9.9 22.1-22.1s-9.9-22.1-22.1-22.1c-12.3.1-22.1 9.9-22.1 22.1m-88.3 0c0 12.2 9.9 22.1 22.1 22.1s22.1-9.9 22.1-22.1s-9.9-22.1-22.1-22.1c-12.2.1-22.1 9.9-22.1 22.1m22.1-6.1c0 3.9 3.2 7.1 7.1 7.1s7.1-3.2 7.1-7.1s-3.2-7.1-7.1-7.1s-7.1 3.2-7.1-7.1m88.2 0c0 3.9 3.2 7.1 7.1 7.1s7.1-3.2 7.1-7.1s-3.2-7.1-7.1-7.1s-7.1 3.2-7.1 7.1" />
                <path fill="#00A8B5" d="m229.5 150.1l26.5 44.1l26.5-44.1zM194.2 459c29.3 0 53 11.9 53 26.5s-23.7 26.5-53 26.5s-53-11.9-53-26.5s23.8-26.5 53-26.5m123.6 0c29.3 0 53 11.9 53 26.5S347 512 317.8 512c-29.3 0-53-11.9-53-26.5s23.7-26.5 53-26.5" />
            </svg>
        </div>
        <h1 class="gradient-page-title">Satış Analiz Dashboard</h1>
    </div>
""",
    unsafe_allow_html=True,
)
    
ROW1_CARD_HEIGHT = 210
ROW2_CARD_HEIGHT = 250


def render_dashboard_body(current_df, sales_df, active_filters, monthly_chart_df=None):
    row1_col1, row1_col2 = st.columns(2, gap="small")

    # ----- 1. KART: Gauge (Yarım Daireler) -----
    with row1_col1:
        with st.container(height=ROW1_CARD_HEIGHT, border=True, key="dashboard-card-gauge"):
            pl_share = get_amount_share(current_df, "pl_status")
            type_share = get_amount_share(current_df, "product_type")
            render_gauge_pair(pl_share, type_share)

    # ----- 2. KART: Donut (Ürün Ciro Dağılımı) -----
    with row1_col2:
        with st.container(height=ROW1_CARD_HEIGHT, border=True, key="dashboard-card-donut"):
            selected_city = active_filters["city"]
            selected_customer = active_filters["customer"]
            selected_product = active_filters.get("product", "Hepsi")

            if selected_product != "Hepsi":

                # Kart başlığı
                if selected_customer != "Hepsi":
                    title = f"Ürünün {selected_customer} Cİro Sıralaması"

                elif selected_city != "Hepsi":
                    title = f"Ürünün {selected_city} Cİro Sıralaması"

                else:
                    title = "Ürünün Ulusal Cİro Sıralaması"

                ranking_df = sales_df.copy()

                if selected_city != "Hepsi":
                    ranking_df = ranking_df[
                        ranking_df["city"] == selected_city
                    ]

                if selected_customer != "Hepsi":
                    ranking_df = ranking_df[
                        ranking_df["customer_name"] == selected_customer
                    ]

                summary = build_product_summary_rank(
                    ranking_df,
                    selected_product,
                )

                if summary is not None:
                    render_product_summary_rank(
                        title=title,
                        rank=summary["rank"],
                        total=summary["total"],
                        percentile=summary["percentile"],
                    )

            else:

                render_donut_chart(
                    title="Ürün Ciro Dağılımı",
                    chart_df=build_product_revenue_share_table(
                        current_df,
                        top_n=8,
                        others_label="Diğer",
                    ),
                    label_col="product_name",
                    value_col="total_amount",
                )

    # ==========================================
    # 2. BÖLÜM: Ürün seçiliyken 2 geniş sütun (Bölgesel kart gereksiz),
    # aksi halde 3 eşit sütun, yan yana, üst satıra yakın (başlık yok)
    # ==========================================
    row2_selected_product = active_filters.get("product", "Hepsi")
    row2_has_city_card = row2_selected_product == "Hepsi"
    row2_col3 = None

    if row2_has_city_card:
        row2_col1, row2_col2, row2_col3 = st.columns(3, gap="small")
    else:
        row2_col1, row2_col2 = st.columns(2, gap="small")

    # ----- 3. KART: Aylık Performans (Çizgi/Sütun Grafik) -----
    with row2_col1:
        with st.container(height=ROW2_CARD_HEIGHT, border=True, key="dashboard-card-monthly"):
            render_monthly_chart_card(
                monthly_chart_df if monthly_chart_df is not None else current_df,
                active_filters or {},
            )

    # ----- 4. KART: Müşteri Performansı -----
    with row2_col2:
        customer_type = st.session_state.get("performance_type_customer", "Ciro")
        customer_value_col = "total_amount" if customer_type == "Ciro" else "quantity"
        customer_value_label = "Ciro" if customer_type == "Ciro" else "Kilogram"
        customer_value_suffix = " ₺" if customer_type == "Ciro" else ""

        customer_ranking = build_ranked_table(
            current_df,
            "customer_name",
            customer_value_col,
            group_label="Müşteri",
            value_label=customer_value_label,
        )

        with st.container(height=ROW2_CARD_HEIGHT, border=True, key="dashboard-card-customer"):
            selected_customer = active_filters["customer"]
            if selected_customer != "Hepsi":
                summary = build_customer_invoice_summary(
                    current_df,
                    sales_df,
                    selected_customer
                )

                if summary is not None:
                    render_customer_invoice_summary(
                        avg_invoice=summary["avg_invoice"],
                        difference=summary["difference"],
                        status=summary["status"],
                    )
            else:
                render_horizontal_bar_chart(
                    title="Müşteri Performansı",
                    chart_df=customer_ranking,
                    label_col="Müşteri",
                    value_col=customer_value_label,
                    value_suffix=customer_value_suffix,
                    render_controls=lambda: render_chart_controls("performance_type_customer"),
                )

    # ----- 5. KART: Bölgesel Performans (sadece ürün seçili değilken gösterilir) -----
    if row2_has_city_card and row2_col3 is not None:
        with row2_col3:
            city_type = st.session_state.get("performance_type_city", "Ciro")
            city_value_col = "total_amount" if city_type == "Ciro" else "quantity"
            city_value_label = "Ciro" if city_type == "Ciro" else "Kilogram"
            city_value_suffix = " ₺" if city_type == "Ciro" else ""

            with st.container(height=ROW2_CARD_HEIGHT, border=True, key="dashboard-card-city"):

                selected_city = active_filters["city"]

                if selected_city != "Hepsi":

                    summary = build_city_summary_rank(sales_df, selected_city)

                    if summary:
                        render_city_summary_rank(
                            rank=summary["rank"],
                            total=summary["total"],
                            difference=summary["difference"],
                            status=summary["status"],
                        )

                else:

                    city_ranking = build_ranked_table(
                        current_df,
                        "city",
                        city_value_col,
                        group_label="İl",
                        value_label=city_value_label,
                    )

                    render_horizontal_bar_chart(
                        title="Bölgesel Performans",
                        chart_df=city_ranking,
                        label_col="İl",
                        value_col=city_value_label,
                        value_suffix=city_value_suffix,
                        render_controls=lambda: render_chart_controls("performance_type_city"),
                    )
