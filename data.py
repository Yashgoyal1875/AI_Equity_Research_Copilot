
import yfinance as yf
import streamlit as st
import time


@st.cache_data(ttl=3600)
def get_company_data(stock):

    for _ in range(3):

        try:

            company = yf.Ticker(stock)

            info = company.info

            return company, info

        except Exception:

            time.sleep(2)

    raise Exception(
        "Yahoo Finance rate limit reached"
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
