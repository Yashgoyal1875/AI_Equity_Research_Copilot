
from alpha_vantage.fundamentaldata import FundamentalData

import yfinance as yf
import streamlit as st


api_key = st.secrets[
    "ALPHA_VANTAGE_API_KEY"
]

fd = FundamentalData(
    key=api_key,
    output_format="pandas"
)


@st.cache_data(ttl=3600)
def get_company_data(stock):

    overview, _ = fd.get_company_overview(
        stock
    )

    return overview


@st.cache_data(ttl=3600)
def get_stock_history(stock):

    data = yf.download(
        stock,
        period="1y"
    )

    data = data.reset_index()

    return data
