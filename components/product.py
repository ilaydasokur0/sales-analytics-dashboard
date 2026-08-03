import streamlit as st

def render_product_summary_rank(title, rank, total, percentile):
    is_above = percentile >= 50
    icon = "▲" if is_above else "▼"
    benchmark_class = "benchmark-up" if is_above else "benchmark-down"
    line_color = "#16A34A" if is_above else "#DC2626"
    status_text = "İlk %50'lik dilimde" if is_above else "Son %50'lik dilimde"

    st.markdown(
        f"""
        <div class="city-rank-card">
            <div class="city-rank-title">{title}</div>
            <div class="city-rank-number">#{rank} <span>/{total}</span></div>
            <div class="city-rank-sparkline-wrap">
                <svg viewBox="0 0 200 50" preserveAspectRatio="none">
                    <defs>
                        <linearGradient id="sparklineGradProd" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="0%" stop-color="{line_color}" stop-opacity="0.25" />
                            <stop offset="100%" stop-color="{line_color}" stop-opacity="0.0" />
                        </linearGradient>
                    </defs>
                    <path d="M0,35 Q30,15 60,30 T120,10 T180,38 T200,20 L200,50 L0,50 Z" fill="url(#sparklineGradProd)" />
                    <path d="M0,35 Q30,15 60,30 T120,10 T180,38 T200,20" fill="none" stroke="{line_color}" stroke-width="2.5" stroke-linecap="round" />
                </svg>
            </div>
            <div class="city-rank-benchmark {benchmark_class}">
                <span class="benchmark-icon">{icon}</span>
                <span>{status_text}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )