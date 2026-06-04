import yfinance as yf
import streamlit as st


@st.cache_data(ttl=3600)
def get_company_data(stock):

    ticker = yf.Ticker(stock)

    info = ticker.info

    return {
        "Name": info.get("longName", stock),
        "Sector": info.get("sector", "Unknown"),
        "MarketCapitalization": info.get("marketCap", 0),
        "PERatio": info.get("trailingPE", 0)
    }


@st.cache_data(ttl=3600)
def get_stock_history(stock):

    data = yf.download(
        stock,
        period="1y",
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        return data

    if hasattr(data.columns, "droplevel"):
        try:
            data.columns = data.columns.droplevel(1)
        except:
            pass

    data = data.reset_index()

    return data