
<<<<<<< HEAD
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
=======
import yfinance as yf
import streamlit as st
import time

>>>>>>> 6c7a965ebea8c8134cd2b0c9e8d755157b61266e

@st.cache_data(ttl=3600)
def get_company_data(stock):

<<<<<<< HEAD
    overview, _ = fd.get_company_overview(
        stock
    )

    return overview
=======
    for _ in range(3):

        try:

            company = yf.Ticker(stock)
>>>>>>> 6c7a965ebea8c8134cd2b0c9e8d755157b61266e

            info = company.info

<<<<<<< HEAD
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
=======
            return company, info

        except Exception:

            time.sleep(2)

    raise Exception(
        "Yahoo Finance rate limit reached"
>>>>>>> 6c7a965ebea8c8134cd2b0c9e8d755157b61266e
    )


@st.cache_data(ttl=3600)
def get_stock_history(stock):

    for _ in range(3):

        try:

            data = yf.download(
                stock,
                period="1y"
            )

            return data

        except Exception:

            time.sleep(2)

    raise Exception(
        "Stock history unavailable"
    )


@st.cache_data(ttl=3600)
def get_financial_statements(stock):

<<<<<<< HEAD
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

=======
    for _ in range(3):

        try:

            company = yf.Ticker(stock)

            financials = company.financials

            balance_sheet = company.balance_sheet

            cashflow = company.cashflow

            return (
                financials,
                balance_sheet,
                cashflow
            )

        except Exception:

            time.sleep(2)

    raise Exception(
        "Financial statements unavailable"
    )
>>>>>>> 6c7a965ebea8c8134cd2b0c9e8d755157b61266e
