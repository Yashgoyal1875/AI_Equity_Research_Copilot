from alpha_vantage.fundamentaldata import FundamentalData
import yfinance as yf
import streamlit as st
import pandas as pd


alpha_key = st.secrets["ALPHA_VANTAGE_API_KEY"]

fd = FundamentalData(
    key=alpha_key,
    output_format="pandas"
)


@st.cache_data(ttl=86400)
def get_company_data(stock):

    try:

        overview, _ = fd.get_company_overview(
            stock
        )

        if overview.empty:

            return {
                "Name": stock,
                "Sector": "Unknown",
                "MarketCapitalization": 0,
                "PERatio": 0
            }

        return {
            "Name": overview["Name"].values[0],
            "Sector": overview["Sector"].values[0],
            "MarketCapitalization": float(
                overview["MarketCapitalization"].values[0]
            )
            if overview["MarketCapitalization"].values[0]
            else 0,
            "PERatio": float(
                overview["PERatio"].values[0]
            )
            if overview["PERatio"].values[0]
            else 0
        }

    except Exception as e:

        print("Alpha Vantage Error:", e)

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

        if data.empty:
            return pd.DataFrame()

        data = data.reset_index()

        if hasattr(data.columns, "droplevel"):

            try:
                data.columns = [
                    col[0]
                    if isinstance(col, tuple)
                    else col
                    for col in data.columns
                ]
            except:
                pass

        return data

    except Exception as e:

        print("Yahoo Error:", e)

        return pd.DataFrame()