import streamlit as st
from services import analysis as sa
from services.formatters import format_currency
from utils.metrics import get_city_share, get_customer_city_share


def render_delta_metric(
    label,
    current_value,
    previous_value,
    formatter,
    *,
    show_percentage=True,
    comparison_enabled=True,
):
    if not comparison_enabled:
        st.metric(label, formatter(current_value))
        return

    if previous_value == 0:
        st.metric(label, formatter(current_value), delta="Karşılaştırma verisi yok", delta_color="off")
        return

    if show_percentage:
        change_ratio = ((current_value - previous_value) / previous_value) * 100
        delta = f"{change_ratio:+.1f}%"
    else:
        delta = f"{current_value - previous_value:+,.0f}"

    st.metric(
        label,
        formatter(current_value),
        delta=delta,
    )

def render_share_metrics(share_series):
    if share_series.empty:
        st.info("Veri bulunamadı.")
        return

    # If there's only one category (e.g., a single product selected), show only the label
    if len(share_series) == 1:
        label = share_series.index[0]
        col = st.columns(1, gap="small")[0]
        with col:
            st.markdown(
                f'<div class="distribution-selected-value">{label}</div>',
                unsafe_allow_html=True,
            )
        return

    cols = st.columns(len(share_series), gap="small")

    for col, (label, value) in zip(cols, share_series.items()):
        with col:
            st.metric(label, f"%{value:.2f}")

def get_trend_arrow(current_value, previous_value, comparison_enabled=True):
    if not comparison_enabled or previous_value is None:
        return ""
    if current_value > previous_value:
        return "▲"
    if current_value < previous_value:
        return "▼"
    return ""


def render_kpi_section(
    current_month_df,
    previous_month_df,
    city_base_df,
    national_df,
    active_filters,
    comparison_enabled,
):
    with st.container(border=True):
        row1_col1, row1_col2, row1_col3 = st.columns(3, gap="small")

        with row1_col1:
            render_delta_metric(
                "Toplam Ciro",
                sa.get_total_sales(current_month_df),
                sa.get_total_sales(previous_month_df),
                format_currency,
                comparison_enabled=comparison_enabled,
            )

        with row1_col2:
            render_delta_metric(
                "Toplam Satış Adedi",
                sa.get_total_quantity(current_month_df),
                sa.get_total_quantity(previous_month_df),
                lambda value: f"{value:,}",
                comparison_enabled=comparison_enabled,
            )

        with row1_col3:
            render_delta_metric(
                "Ortalama Fatura Tutarı",
                sa.get_average_invoice_amount(current_month_df),
                sa.get_average_invoice_amount(previous_month_df),
                format_currency,
                comparison_enabled=comparison_enabled,
            )

        st.markdown('<div style="height:.18rem"></div>', unsafe_allow_html=True)

        row2_col1, row2_col2, row2_col3 = st.columns(3, gap="small")

        city_and_customer_selected = (
            active_filters["city"] != "Hepsi" and active_filters["customer"] != "Hepsi"
        )
        city_and_customer_and_product_selected = (
            active_filters["city"] != "Hepsi"
            and active_filters["customer"] != "Hepsi"
            and active_filters.get("product", "Hepsi") != "Hepsi"
        )

        with row2_col1:
            if city_and_customer_and_product_selected:
                render_delta_metric(
                    "Ürünün Müşterideki Ciro Payı",
                    sa.get_customer_product_share(city_base_df, current_month_df, active_filters),
                    sa.get_customer_product_share(city_base_df, previous_month_df, active_filters),
                    lambda value: f"%{value:.1f}",
                    show_percentage=False,
                    comparison_enabled=comparison_enabled,
                )
            
            elif city_and_customer_selected:
                render_delta_metric(
                    "Alınan Ürün Çeşitliliği",
                    sa.get_total_product_count(current_month_df),
                    sa.get_total_product_count(previous_month_df),
                    lambda value: f"{value:,}",
                    show_percentage=False,
                    comparison_enabled=comparison_enabled,
                )
            
                
            else:
                render_delta_metric(
                    "Aktif Müşteri",
                    sa.get_total_customer_count(current_month_df),
                    sa.get_total_customer_count(previous_month_df),
                    lambda value: f"{value:,}",
                    show_percentage=False,
                    comparison_enabled=comparison_enabled,
                )

        with row2_col2:
            render_delta_metric(
                "Fatura Sayısı",
                sa.get_total_invoice_count(current_month_df),
                sa.get_total_invoice_count(previous_month_df),
                lambda value: f"{value:,}",
                show_percentage=False,
                comparison_enabled=comparison_enabled,
            )

        with row2_col3:
            if city_and_customer_and_product_selected:
                render_delta_metric(
                    "Müşterinin Üründeki Ciro Payı",
                    sa.get_product_customer_share(current_month_df, active_filters),
                    sa.get_product_customer_share(previous_month_df, active_filters),
                    lambda value: f"%{value:.1f}",
                    show_percentage=False,
                    comparison_enabled=comparison_enabled,
                )

            elif city_and_customer_selected:
                customer_city_share = get_customer_city_share(city_base_df, current_month_df)
                st.metric("Müşterinin İldeki Ciro Payı", f"%{customer_city_share:.1f}")

            elif active_filters["city"] != "Hepsi":
                city_share = get_city_share(national_df, current_month_df)
                st.metric("İlin Ulusal Ciro Payı", f"%{city_share:.1f}")

            else:
                render_delta_metric(
                    "Satış Yapılan Şehir",
                    sa.get_total_city_count(current_month_df),
                    sa.get_total_city_count(previous_month_df),
                    lambda value: f"{value:,}",
                    show_percentage=False,
                    comparison_enabled=comparison_enabled,
                )