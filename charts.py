
import plotly.graph_objects as go
import streamlit as st

def create_stock_chart(data):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"].squeeze(),
            mode="lines",
            name="Stock Price"
        )
    )

    fig.update_layout(
        title="1 Year Stock Price Trend",
        template="plotly_dark",
        height=600,
        xaxis_title="Date",
        yaxis_title="Price"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def create_revenue_chart(revenue):

    revenue_fig = go.Figure()

    revenue_fig.add_trace(
        go.Bar(
            x=revenue.index.astype(str),
            y=revenue.values,
            name="Revenue"
        )
    )

    revenue_fig.update_layout(
        title="Revenue Trend",
        template="plotly_dark"
    )

    st.plotly_chart(
        revenue_fig,
        use_container_width=True
    )


def create_profit_chart(net_income):

    profit_fig = go.Figure()

    profit_fig.add_trace(
        go.Bar(
            x=net_income.index.astype(str),
            y=net_income.values,
            name="Net Profit"
        )
    )

    profit_fig.update_layout(
        title="Net Profit Trend",
        template="plotly_dark"
    )

    st.plotly_chart(
        profit_fig,
        use_container_width=True
    )
