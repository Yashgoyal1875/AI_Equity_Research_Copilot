import yfinance as yf
import streamlit as st


@st.cache_data(ttl=86400)
def get_company_data(stock):

    try:

        ticker = yf.Ticker(stock)

        info = ticker.info

        return {
            "Name": info.get("longName", stock),
            "Sector": info.get("sector", "Unknown"),
            "MarketCapitalization": info.get("marketCap", 0),
            "PERatio": info.get("trailingPE", 0)
        }

    except Exception:

        return {
            "Name": stock,
            "Sector": "Unknown",
            "MarketCapitalization": 0,
            "PERatio": 0
        }


@st.cache_data(ttl=86400)
def get_stock_history(stock):

    try:

        data = yf.download(
            stock,
            period="1y",
            auto_adjust=True,
            progress=False
        )

        data = data.reset_index()

        if hasattr(data.columns, "droplevel"):

            try:
                data.columns = [
                    col[0] if isinstance(col, tuple)
                    else col
                    for col in data.columns
                ]
            except:
                pass

        return data

    except Exception:

        import pandas as pd

        return pd.DataFrame()