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
        '<div class="page-title">Satış Analiz Dashboard</div>',
        unsafe_allow_html=True,
    )

ROW1_CARD_HEIGHT = 210
ROW2_CARD_HEIGHT = 250


def render_dashboard_body(current_df, sales_df, active_filters, monthly_chart_df=None):
    row1_col1, row1_col2 = st.columns(2, gap="small")

    # ----- 1. KART: Gauge (Yarım Daireler) -----
    with row1_col1:
        with st.container(height=ROW1_CARD_HEIGHT, border=True):
            pl_share = get_amount_share(current_df, "pl_status")
            type_share = get_amount_share(current_df, "product_type")
            render_gauge_pair(pl_share, type_share)

    # ----- 2. KART: Donut (Ürün Ciro Dağılımı) -----
    with row1_col2:
        with st.container(height=ROW1_CARD_HEIGHT, border=True):
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
        with st.container(height=ROW2_CARD_HEIGHT, border=True):
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

        with st.container(height=ROW2_CARD_HEIGHT, border=True):
            selected_customer = active_filters["customer"]
            if selected_customer != "Hepsi":
                summary = build_customer_invoice_summary(
                    current_df,
                    sales_df,
                    selected_customer
                )

                if summary is not None:
                    st.html('<div style="flex-grow: 1;"></div>')
                    render_customer_invoice_summary(
                        avg_invoice=summary["avg_invoice"],
                        difference=summary["difference"],
                        status=summary["status"],
                    )
                    st.html('<div style="flex-grow: 1;"></div>')
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

            with st.container(height=ROW2_CARD_HEIGHT, border=True):

                selected_city = active_filters["city"]

                if selected_city != "Hepsi":

                    summary = build_city_summary_rank(sales_df, selected_city)

                    if summary:
                        st.html('<div style="flex-grow: 1;"></div>')
                        render_city_summary_rank(
                            rank=summary["rank"],
                            total=summary["total"],
                            difference=summary["difference"],
                            status=summary["status"],
                        )
                        st.html('<div style="flex-grow: 1;"></div>')

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