import streamlit as st


def render_product_summary_rank(title, rank, total, percentile):

    if percentile <= 10:
        badge = "İlk %10"
        color = "#16A34A"

    elif percentile <= 25:
        badge = "İlk %25"
        color = "#22C55E"

    elif percentile <= 50:
        badge = "İlk %50"
        color = "#F59E0B"

    else:
        badge = "Alt %50"
        color = "#DC2626"

    st.markdown(
        f"""
        <div class="city-rank-card">
            <div class="city-rank-title">
                {title}
            </div>
            <div class="city-rank-number">
                #{rank}<span> / {total}</span>
            </div>
            <div class="city-rank-benchmark"
                 style="color:{color};">
                {badge}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )