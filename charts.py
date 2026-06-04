import plotly.express as px
import streamlit as st


def create_stock_chart(data):

    if data.empty:

        st.error(
            "No stock history available."
        )

        return

    if "Date" not in data.columns:

        st.error(
            f"Date column missing. Available columns: {list(data.columns)}"
        )

        return

    if "Close" not in data.columns:

        st.error(
            f"Close column missing. Available columns: {list(data.columns)}"
        )

        return

    fig = px.line(
        data,
        x="Date",
        y="Close",
        title="1 Year Stock Price Trend"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )