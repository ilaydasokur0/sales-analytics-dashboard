import streamlit as st
from components.charts import (
    render_chart_controls,
    render_donut_chart,
    render_horizontal_bar_chart,
    render_monthly_chart_card,
    render_product_info_card,
    render_gauge_pair
)
from services.analysis import get_amount_share
from utils.tables import build_product_revenue_share_table, build_ranked_table


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
    elif (
        active_filters["start_date"] == sales_df["invoice_date"].min().date()
        and active_filters["end_date"] == sales_df["invoice_date"].max().date()
    ):
        st.caption("Seçilen tarih aralığı için karşılaştırma yapılamıyor.")

    if active_filters["month_label"] != "Hepsi" and not active_filters["comparison_available"]:
        st.caption("Seçilen ay için karşılaştırma yapılamıyor.")

    if current_month_df.empty:
        st.warning("Seçilen filtrelerde veri bulunamadı. Filtreleri genişletip tekrar deneyin.")
        st.stop()


def render_dashboard_body(current_df, active_filters, monthly_chart_df=None):
    """
    Tüm dashboard ekran kartlarının düzenini (layout) yöneten tek ana gövde fonksiyonu.
    Sıralamayı veya sütun düzenini değiştirmek için aşağıdaki blokların yerini değiştirmeniz yeterlidir.

    NOT: city_selected / customer_selected özel durumlarına göre farklı görünümler
    (ör. müşteri/il bazlı özel tablolar) şu an bu taslakta yok; bu kısım daha
    sonra ayrıca ele alınacak. Şimdilik şablon sabit.
    """

    # ==========================================
    # 1. BÖLÜM: ÜST KARTLAR (2 Sütunlu Yapı)
    # ==========================================
    row1_col1, row1_col2 = st.columns(2, gap="small")

    # ----- 1. KART: Gauge (Yarım Daireler) -----
    with row1_col1:
        with st.container(border=True):
            city_selected = active_filters["city"] != "Hepsi"
            customer_selected = active_filters["customer"] != "Hepsi"
            product_selected = active_filters.get("product", "Hepsi") != "Hepsi"

            if city_selected and customer_selected and product_selected:
                st.markdown('<div class="section-title section-title--large">Ürün Özellikleri</div>', unsafe_allow_html=True)
                render_product_info_card(current_df)
            else:
                st.markdown('<div class="section-title section-title--large">Ürün Tipi ve PL Dağılımları</div>', unsafe_allow_html=True)
                pl_share = get_amount_share(current_df, "pl_status")
                type_share = get_amount_share(current_df, "product_type")
                render_gauge_pair(pl_share, type_share)

    # ----- 2. KART: Donut (Ürün Ciro Dağılımı) -----
    with row1_col2:
        with st.container(border=True):
            render_donut_chart(
                title="Ürün Ciro Dağılımı",
                chart_df=build_product_revenue_share_table(current_df, top_n=8, others_label="Diğer"),
                label_col="product_name",
                value_col="total_amount",
            )

    # ==========================================
    # 2. BÖLÜM: ALT KARTLAR (2 Sütunlu Performans Özeti)
    # row2_col2 kendi içinde ikiye ayrılır: üstte Müşteri Performansı,
    # altta Bölgesel (İl) Performans yatay bar grafiği.
    # ==========================================
    st.subheader("Performans Özeti")
    row2_col1, row2_col2 = st.columns(2, gap="small")

    # ----- 3. KART: Aylık Performans (Çizgi/Sütun Grafik) -----
    with row2_col1:
        with st.container(height=260, border=True):
            render_monthly_chart_card(
                monthly_chart_df if monthly_chart_df is not None else current_df,
                active_filters or {},
            )

    # ----- 4. KART: row2_col2 içinde ikiye bölünmüş performans barları -----
    with row2_col2:
        # ---- 4a. Müşteri Performansı (üstte) ----
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
        with st.container(height=125, border=True):
            render_horizontal_bar_chart(
                title="Müşteri Performansı",
                chart_df=customer_ranking,
                label_col="Müşteri",
                value_col=customer_value_label,
                value_suffix=customer_value_suffix,
                render_controls=lambda: render_chart_controls("performance_type_customer"),
            )

        # ---- 4b. Bölgesel (İl) Performans (altta) ----
        city_type = st.session_state.get("performance_type_city", "Ciro")
        city_value_col = "total_amount" if city_type == "Ciro" else "quantity"
        city_value_label = "Ciro" if city_type == "Ciro" else "Satış Adedi"
        city_value_suffix = " ₺" if city_type == "Ciro" else ""

        city_ranking = build_ranked_table(
            current_df,
            "city",
            city_value_col,
            group_label="İl",
            value_label=city_value_label,
        )
        with st.container(height=125, border=True):
            render_horizontal_bar_chart(
                title="Bölgesel Performans",
                chart_df=city_ranking,
                label_col="İl",
                value_col=city_value_label,
                value_suffix=city_value_suffix,
                render_controls=lambda: render_chart_controls("performance_type_city"),
            )