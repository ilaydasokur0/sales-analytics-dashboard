import streamlit as st
from components.charts import (
    render_chart_controls,
    render_donut_chart,
    render_horizontal_bar_chart,
    render_monthly_chart_card,
    render_product_info_card,
    render_gauge_pair,
)
from components.city import render_city_summary_rank
from services.analysis import get_amount_share
from utils.tables import build_city_summary_rank, build_product_revenue_share_table, build_ranked_table

def render_header(
    sales_df,
    active_filters,
    comparison_enabled,
    current_period,
    previous_period,
    current_month_df,
):
    st.markdown('<div class="page-title">Satış Analiz ve Raporlama Sistemi</div>', unsafe_allow_html=True)

    if comparison_enabled:
        st.caption(f"Karşılaştırma: {current_period} / {previous_period}")

    if active_filters["month_label"] != "Hepsi" and not active_filters["comparison_available"]:
        st.caption("Seçilen ay için karşılaştırma yapılamıyor.")

    if current_month_df.empty:
        st.warning("Seçilen filtrelerde veri bulunamadı. Filtreleri genişletip tekrar deneyin.")
        st.stop()


# Row1 ve Row2 kartlarının hepsi bu sabit yüksekliklerle hizalanır.
ROW1_CARD_HEIGHT = 205
ROW2_CARD_HEIGHT = 195


def render_dashboard_body(current_df, sales_df, active_filters, monthly_chart_df=None):
   
    # ==========================================
    # 1. BÖLÜM: ÜST KARTLAR (Eşit Genişlik: Gauge / Donut)
    # ==========================================
    row1_col1, row1_col2 = st.columns(2, gap="small")

    # ----- 1. KART: Gauge (Yarım Daireler) -----
    with row1_col1:
        with st.container(height=ROW1_CARD_HEIGHT, border=True):
            city_selected = active_filters["city"] != "Hepsi"
            customer_selected = active_filters["customer"] != "Hepsi"
            product_selected = active_filters.get("product", "Hepsi") != "Hepsi"

            if city_selected and customer_selected and product_selected:
                st.markdown('<div class="section-title section-title--large">Ürün Özellikleri</div>', unsafe_allow_html=True)
                render_product_info_card(current_df)
            else:
                st.markdown('<div class="gauge-card-body">', unsafe_allow_html=True)
                st.markdown('<div class="section-title section-title--large">Ürün Tipi ve PL Dağılımları</div>', unsafe_allow_html=True)
                pl_share = get_amount_share(current_df, "pl_status")
                type_share = get_amount_share(current_df, "product_type")
                render_gauge_pair(pl_share, type_share)
                st.markdown('</div>', unsafe_allow_html=True)

    # ----- 2. KART: Donut (Ürün Ciro Dağılımı) -----
    with row1_col2:
        with st.container(height=ROW1_CARD_HEIGHT, border=True):
            render_donut_chart(
                title="Ürün Ciro Dağılımı",
                chart_df=build_product_revenue_share_table(current_df, top_n=8, others_label="Diğer"),
                label_col="product_name",
                value_col="total_amount",
            )

    # ==========================================
    # 2. BÖLÜM: 3 eşit sütun, yan yana, üst satıra yakın (başlık yok)
    # ==========================================
    row2_col1, row2_col2, row2_col3 = st.columns(3, gap="small")

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
        customer_value_label = "Ciro" if customer_type == "Ciro" else "Satış Adedi"
        customer_value_suffix = " ₺" if customer_type == "Ciro" else ""

        customer_ranking = build_ranked_table(
            current_df,
            "customer_name",
            customer_value_col,
            group_label="Müşteri",
            value_label=customer_value_label,
        )
        with st.container(height=ROW2_CARD_HEIGHT, border=True):
            render_horizontal_bar_chart(
                title="Müşteri Performansı",
                chart_df=customer_ranking,
                label_col="Müşteri",
                value_col=customer_value_label,
                value_suffix=customer_value_suffix,
                render_controls=lambda: render_chart_controls("performance_type_customer"),
            )

    # ----- 5. KART: Bölgesel Performans -----
    with row2_col3:
        city_type = st.session_state.get("performance_type_city", "Ciro")
        city_value_col = "total_amount" if city_type == "Ciro" else "quantity"
        city_value_label = "Ciro" if city_type == "Ciro" else "Satış Adedi"
        city_value_suffix = " ₺" if city_type == "Ciro" else ""

        with st.container(height=ROW2_CARD_HEIGHT, border=True):

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