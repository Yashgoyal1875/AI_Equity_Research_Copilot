
import plotly.express as px
import streamlit as st


def create_stock_chart(data):

    if data.empty:

        st.error(
            "No stock data available"
        )

        return

    data.columns = [
        col[0] if isinstance(col, tuple)
        else col
        for col in data.columns
    ]

    if "Date" not in data.columns:

        data = data.reset_index()

    fig = px.line(
        data,
        x="Date",
        y="Close",
        title="1 Year Stock Price Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
