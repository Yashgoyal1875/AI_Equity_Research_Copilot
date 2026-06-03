
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

import streamlit as st
import pandas as pd

api_key = st.secrets[
    "ALPHA_VANTAGE_API_KEY"
]

ts = TimeSeries(
    key=api_key,
    output_format="pandas"
)

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

    data, meta = ts.get_daily_adjusted(
        symbol=stock,
        outputsize="compact"
    )

    data = data.reset_index()

    data.rename(
        columns={
            "date": "Date",
            "4. close": "Close"
        },
        inplace=True
    )

    return data


@st.cache_data(ttl=3600)
def get_financial_statements(stock):

    income_statement, _ = (
        fd.get_income_statement_annual(
            stock
        )
    )

    balance_sheet, _ = (
        fd.get_balance_sheet_annual(
            stock
        )
    )

    cashflow, _ = (
        fd.get_cash_flow_annual(
            stock
        )
    )

    return (
        income_statement,
        balance_sheet,
        cashflow
    )

