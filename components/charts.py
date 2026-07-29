import streamlit as st
import pandas as pd
import altair as alt
import services.analysis as sa
from components.kpi import render_share_metrics
from services.analysis import get_amount_share
from services.formatters import format_currency
from utils.tables import build_selected_product_info
import html
import textwrap

def render_chart_controls(graph_key):
    return st.radio(
        "Grafik Türü",
        ["Ciro", "Satış Adedi"],
        horizontal=True,
        key=graph_key,
        label_visibility="collapsed",
    )

def get_chart_data(df, graph_type):
    if graph_type == "Ciro":
        return sa.get_monthly_sales(df)

    return sa.get_monthly_quantity(df)

def render_product_info_card(filtered_df):
    info_items = build_selected_product_info(filtered_df)
    if not info_items:
        st.info("Veri bulunamadı.")
        return

    for index, (label, value) in enumerate(info_items):
        left_col, right_col = st.columns([1, 1.1], gap="small")

        with left_col:
            st.markdown(
                f'<div class="product-info-label">{label}</div>',
                unsafe_allow_html=True,
            )

        with right_col:
            st.markdown(
                f'<div class="product-info-value">{value}</div>',
                unsafe_allow_html=True,
            )

        if index != len(info_items) - 1:
            st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)


# ---------------- AYLIK PERFORMANS GRAFİĞİ ---------------- #

def render_monthly_performance_chart(chart_series, is_single_month=False, selected_month_key=None):

    chart_df = chart_series.reset_index()
    chart_df.columns = ["year_month", "value"]

    if chart_df.empty:
        st.info("Veri bulunamadı.")
        return

    if is_single_month:
        chart_df["highlight"] = chart_df["year_month"].apply(
            lambda x: "Seçili Ay" if x == selected_month_key else "Diğer Aylar"
        )
        color_scale = alt.Scale(
            domain=["Seçili Ay", "Diğer Aylar"],
            range=["#0F2E4F", "#C7D6E5"],
        )
        bar_chart = (
            alt.Chart(chart_df)
            .mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
            .encode(
                x=alt.X(
                    "year_month:N",
                    title=None,
                    sort=None,
                    axis=alt.Axis(labelAngle=0, labelFontSize=8, labelPadding=1),
                ),
                y=alt.Y(
                    "value:Q",
                    title=None,
                    axis=alt.Axis(labelFontSize=8, labelPadding=1, tickCount=3),
                ),
                color=alt.Color("highlight:N", scale=color_scale, legend=None),
                tooltip=["year_month", "value"],
            )
            .properties(
                height=175,
                padding={"left": 2, "right": 2, "top": 2, "bottom": 0},
            )
            .configure_view(strokeWidth=0)
            .configure_axis(grid=False)
        )
        st.altair_chart(bar_chart, use_container_width=True)
        return

    average_value = chart_df["value"].mean()
    max_row = chart_df.loc[chart_df["value"].idxmax()]
    min_row = chart_df.loc[chart_df["value"].idxmin()]

    line_chart = (
        alt.Chart(chart_df)
        .mark_line(
            color="#0F2E4F",
            strokeWidth=1.4,
            point=alt.OverlayMarkDef(color="#0F2E4F", size=28),
        )
        .encode(
            x=alt.X(
                "year_month:N",
                title=None,
                sort=None,
                axis=alt.Axis(labelAngle=0, labelFontSize=8, labelPadding=1),
            ),
            y=alt.Y(
                "value:Q",
                title=None,
                axis=alt.Axis(labelFontSize=8, labelPadding=1, tickCount=3),
            ),
            tooltip=["year_month", "value"],
        )
    )

    average_line = (
        alt.Chart(pd.DataFrame({"average": [average_value]}))
        .mark_rule(strokeDash=[6, 4], color="#E8A0A0", size=2)
        .encode(y="average:Q")
    )

    extremes_df = pd.DataFrame(
        [
            {"year_month": max_row["year_month"], "value": max_row["value"], "tip": "En Yüksek"},
            {"year_month": min_row["year_month"], "value": min_row["value"], "tip": "En Düşük"},
        ]
    )
    extremes_points = (
        alt.Chart(extremes_df)
        .mark_point(size=90, filled=True)
        .encode(
            x=alt.X("year_month:N", sort=None),
            y="value:Q",
            color=alt.Color(
                "tip:N",
                scale=alt.Scale(domain=["En Yüksek", "En Düşük"], range=["#00A8B5", "#F28C8C"]),
                legend=None,
            ),
            tooltip=["tip", "value"],
        )
    )

    combined_chart = (line_chart + average_line + extremes_points).properties(
        height=175,
        padding={"left": 2, "right": 2, "top": 2, "bottom": 0},
    )
    combined_chart = combined_chart.configure_view(strokeWidth=0).configure_axis(grid=False)
    st.altair_chart(combined_chart, use_container_width=True)


def render_monthly_chart_card(chart_source_df, active_filters):

    st.markdown('<div class="section-title section-title--large">Aylık Performans</div>', unsafe_allow_html=True)
    graph_type = render_chart_controls("general_graph")
    chart_data = get_chart_data(chart_source_df, graph_type)

    is_single_month = active_filters.get("month_label", "Hepsi") != "Hepsi"
    selected_month_key = None
    if is_single_month:
        selected_month_key = str(pd.Period(active_filters["start_date"], freq="M"))

    render_monthly_performance_chart(chart_data, is_single_month, selected_month_key)


def render_horizontal_bar_chart(
    title,
    chart_df,
    label_col,
    value_col,
    value_suffix="",
    empty_message="Veri bulunamadı.",
    render_controls=None,
):
    st.markdown(
        f'<div class="section-title section-title--large">{title}</div>',
        unsafe_allow_html=True,
    )

    if render_controls is not None:
        render_controls()

    if chart_df.empty:
        st.info(empty_message)
        return

    max_value = chart_df[value_col].max()

    rows_html = []
    for _, row in chart_df.iterrows():
        label = html.escape(str(row[label_col]))
        value = float(row[value_col])

        width = 0
        if max_value != 0:
            width = (value / max_value) * 100

        rows_html.append(
            textwrap.dedent(f"""
                <div class="horizontal-bar-row">
                    <div class="horizontal-bar-name" title="{label}">{label}</div>
                    <div class="horizontal-bar-track">
                        <div class="horizontal-bar-bar" style="width:{width:.1f}%;"></div>
                    </div>
                    <div class="horizontal-bar-meta">
                        <div class="horizontal-bar-amount">{value:,.0f}{value_suffix}</div>
                    </div>
                </div>
            """).strip(),
        )

    st.markdown(
        f'<div class="horizontal-bar-chart">{"".join(rows_html)}</div>',
        unsafe_allow_html=True,
    )

def _gauge_block_html(title, share_series, color_a, color_b):
    if share_series.empty:
        return (
            f'<div class="gauge-block">'
            f'<div class="mini-section-title">{html.escape(title)}</div>'
            f'<div style="padding-top:1rem;">Veri bulunamadı.</div>'
            f"</div>"
        )

    label_a = html.escape(str(share_series.index[0]))
    value_a = float(share_series.iloc[0])

    label_b = (
        html.escape(str(share_series.index[1]))
        if len(share_series) > 1
        else None
    )

    angle = max(0.0, min(180.0, value_a * 1.8))

    legend_html = f'<span class="gauge-legend-item" style="color:{color_a};">● {label_a}</span>'
    if label_b is not None:
        legend_html += f'<span class="gauge-legend-item" style="color:{color_b};">● {label_b}</span>'

    return textwrap.dedent(f"""
        <div class="gauge-block">
            <div class="mini-section-title">{html.escape(title)}</div>
            <div class="gauge-half-wrap">
                <div class="gauge-half" style="background:conic-gradient(from -90deg at 50% 50%, {color_a} 0deg {angle:.1f}deg, {color_b} {angle:.1f}deg 180deg, transparent 180deg 360deg);"></div>
                <div class="gauge-hole"></div>
                <div class="gauge-center-value">%{value_a:.0f}</div>
            </div>
            <div class="gauge-legend-row">{legend_html}</div>
        </div>
    """).strip()


def render_gauge_pair(pl_share, type_share):
    pl_gauge = _gauge_block_html("PL Dağılımı", pl_share, "#FCBA8B", "#FF8B38")

    type_gauge = _gauge_block_html(
        "Ürün Tipi Dağılımı", type_share, "#6AFF7EFF", "#3B9647FF"
    )

    st.markdown(
        f'<div class="gauge-pair">{pl_gauge}{type_gauge}</div>',
        unsafe_allow_html=True,
    )

def render_donut_chart(
    title,
    chart_df,
    label_col,
    value_col,
    empty_message="Veri bulunamadı.",
):
    st.markdown(
        f'<div class="section-title section-title--large">{title}</div>',
        unsafe_allow_html=True,
    )

    if chart_df.empty:
        st.info(empty_message)
        return

    colors = [
        "#0A2B47",
        "#123C5D",
        "#1E3A5F",
        "#2F5A82",
        "#00A8B5",
        "#3FBEC9",
        "#7CC6D6",
        "#A8D8E0",
        "#B8E3EA",
    ]

    size = 180
    center = size / 2
    radius = 60
    stroke_width = 28
    circumference = 2 * 3.14159265 * radius

    slices = []
    offset = 0.0

    for i, (_, row) in enumerate(chart_df.iterrows()):
        label = html.escape(str(row[label_col]))
        share = float(row["share"])
        color = colors[i % len(colors)]

        dash = (share / 100) * circumference
        gap = circumference - dash

        slices.append(
            f'<circle cx="{center}" cy="{center}" r="{radius}" fill="none" '
            f'stroke="{color}" stroke-width="{stroke_width}" '
            f'stroke-dasharray="{dash:.2f} {gap:.2f}" '
            f'stroke-dashoffset="{-offset:.2f}" '
            f'transform="rotate(-90 {center} {center})" '
            f'style="cursor:pointer;">'
            f'<title>{label} (%{share:.1f})</title>'
            f'</circle>'
        )

        offset += dash

    circle_svg = (
        f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
        + "".join(slices) +
        "</svg>"
    )

    legend_html = ""
    for i, (_, row) in enumerate(chart_df.iterrows()):
        label = html.escape(str(row[label_col]))
        value = float(row[value_col])
        color = colors[i % len(colors)]
        legend_html += (
            f'<div class="donut-chart-row">'
            f'<span class="donut-chart-color" style="background:{color};"></span>'
            f'<div class="donut-chart-text">'
            f'<div class="donut-chart-label">{label}</div>'
            f'<div class="donut-chart-value">{format_currency(value)}</div>'
            f'</div>'
            f'</div>'
        )

    html_content = (
        '<div class="donut-chart">'
        f'<div class="donut-chart-circle" style="position:relative;background:none;">'
        f'{circle_svg}'
        '<div class="donut-chart-center" '
        'style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);"></div>'
        '</div>'
        f'<div class="donut-chart-legend">{legend_html}</div>'
        '</div>'
    )

    st.markdown(html_content, unsafe_allow_html=True)
