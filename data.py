
import yfinance as yf
import streamlit as st

@st.cache_data(ttl=3600)
def get_company_data(stock):

    company = yf.Ticker(stock)

    info = company.info

    return company, info


@st.cache_data(ttl=3600)
def get_stock_history(stock):

    data = yf.download(
        stock,
        period="1y"
    )

    return data


@st.cache_data(ttl=3600)
def get_financial_statements(stock):

    company = yf.Ticker(stock)

    financials = company.financials

    balance_sheet = company.balance_sheet

    cashflow = company.cashflow

    return financials, balance_sheet, cashflow

