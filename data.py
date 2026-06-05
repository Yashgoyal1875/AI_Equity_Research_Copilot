from alpha_vantage.fundamentaldata import FundamentalData
import yfinance as yf
import streamlit as st

api_key = st.secrets["ALPHA_VANTAGE_API_KEY"]

fd = FundamentalData(
    key=api_key,
    output_format="pandas"
)


@st.cache_data(ttl=86400)
def get_company_data(stock):

    try:

        # Indian Stocks
        if stock.endswith(".NS") or stock.endswith(".BO"):

            ticker = yf.Ticker(stock)
            info = ticker.info

            return {
                "Name": info.get(
                    "longName",
                    stock
                ),
                "Sector": info.get(
                    "sector",
                    "Unknown"
                ),
                "MarketCapitalization": info.get(
                    "marketCap",
                    0
                ),
                "PERatio": info.get(
                    "trailingPE",
                    0
                )
            }

        # International Stocks
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
                overview[
                    "MarketCapitalization"
                ].values[0]
            ),
            "PERatio": float(
                overview[
                    "PERatio"
                ].values[0]
            )
        }

    except Exception as e:

        print(
            f"Company Data Error: {e}"
        )

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
            return data

        if hasattr(
            data.columns,
            "droplevel"
        ):

            try:
                data.columns = (
                    data.columns.droplevel(1)
                )
            except:
                pass

        data = data.reset_index()

        return data

    except Exception as e:

        print(
            f"Stock History Error: {e}"
        )

        import pandas as pd

        return pd.DataFrame()