import streamlit as st
from utils.tables import build_ranked_table, build_change_table


def render_ranked_pair(
    current_df,
    previous_df,
    left_title,
    right_title,
    *,
    group_col,
    value_col,
    group_label,
    value_label,
    currency=False,
    top_n=5,
    height=145,
):
    left_table = build_ranked_table(
        current_df,
        group_col,
        value_col,
        top_n=top_n,
        ascending=False,
        group_label=group_label,
        value_label=value_label,
    )

    right_table = build_ranked_table(
        current_df,
        group_col,
        value_col,
        top_n=top_n,
        ascending=True,
        group_label=group_label,
        value_label=value_label,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(left_title)
        st.dataframe(
            left_table,
            hide_index=True,
            width="stretch",
            height=height,
        )

    with col2:
        st.subheader(right_title)
        st.dataframe(
            right_table,
            hide_index=True,
            width="stretch",
            height=height,
        )


def render_overview_section(
    current_df,
    previous_df,
    title,
    group_col,
    value_col,
    group_label,
    value_label,
    *,
    currency=False,
    top_caption="Lider Segmentler",
    bottom_caption="Gelişim Alanları",
):
    st.subheader(title)
    top_table = build_ranked_table(
        current_df,
        group_col,
        value_col,
        top_n=5,
        group_label=group_label,
        value_label=value_label,
    )
    change_table = build_change_table(
        current_df,
        previous_df,
        group_col,
        value_col,
        top_n=5,
        group_label=group_label,
        value_label=value_label,
        currency=currency,
    )
    st.caption(top_caption)
    st.dataframe(top_table, hide_index=True, width="stretch", height=112)
    st.caption(bottom_caption)
    st.dataframe(change_table, hide_index=True, width="stretch", height=112)
