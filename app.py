
from data import (
    get_company_data,
    get_stock_history,
    get_financial_statements
)

from charts import (
    create_stock_chart,
    create_revenue_chart,
    create_profit_chart
)

from analysis import (
    generate_ai_analysis,
    analyze_news_sentiment
)

from news import get_company_news

import streamlit as st

st.set_page_config(
    page_title="AI Equity Research Copilot",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center;
    color: #00FFAA;'>
    AI Equity Research Copilot
    </h1>

    <h4 style='text-align: center;
    color: gray;'>
    AI Powered Financial Intelligence Platform
    </h4>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "## Powered by Gemini AI"
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    "## Dashboard Sections"
)

st.sidebar.markdown(
    """
    • Market Overview  
    • Financial Statements  
    • Business Analytics  
    • AI Investment Analysis  
    • Company News  
    • AI News Sentiment  
    """
)

stock = st.sidebar.text_input(
    "Enter Stock Symbol",
    value="TCS.NS"
)

analyze = st.sidebar.button(
    "Analyze Stock"
)

if analyze:

    with st.spinner(
        "Analyzing company financials and market intelligence..."
    ):

        try:

            company, info = get_company_data(stock)

            st.header(info.get("longName"))

            col1, col2, col3 = st.columns(3)

            market_cap = info.get("marketCap")
            pe_ratio = info.get("trailingPE")
            sector = info.get("sector")

            col1.metric(
                "Business Sector",
                sector
            )

            if market_cap:

                col2.metric(
                    "Market Capitalization",
                    f"{market_cap / 1_000_000_000:.2f} B"
                )

            if pe_ratio:

                col3.metric(
                    "Price to Earnings Ratio",
                    round(pe_ratio, 2)
                )

            data = get_stock_history(stock)

            create_stock_chart(data)

            st.markdown(
                "## Financial Statements"
            )

            financials, balance_sheet, cashflow = (
                get_financial_statements(stock)
            )

            with st.expander("Income Statement"):

                st.dataframe(financials)

            with st.expander("Balance Sheet"):

                st.dataframe(balance_sheet)

            with st.expander("Cash Flow Statement"):

                st.dataframe(cashflow)

            revenue_growth = 0
            profit_margin = 0

            st.markdown(
                "## Business Analytics Dashboard"
            )

            try:

                revenue = financials.loc["Total Revenue"]

                net_income = financials.loc["Net Income"]

                col1, col2 = st.columns(2)

                with col1:

                    create_revenue_chart(revenue)

                with col2:

                    create_profit_chart(net_income)

                st.markdown(
                    "### Key Financial Metrics"
                )

                metric1, metric2 = st.columns(2)

                revenue_growth = (
                    (revenue.iloc[0] - revenue.iloc[1])
                    / revenue.iloc[1]
                ) * 100

                latest_revenue = revenue.iloc[0]

                latest_profit = net_income.iloc[0]

                profit_margin = (
                    latest_profit / latest_revenue
                ) * 100

                with metric1:

                    st.metric(
                        "Latest Revenue Growth %",
                        f"{revenue_growth:.2f}%"
                    )

                with metric2:

                    st.metric(
                        "Profit Margin",
                        f"{profit_margin:.2f}%"
                    )

            except Exception:

                st.warning(
                    "Financial trend data unavailable"
                )

            st.markdown(
                "## AI Investment Analysis"
            )

            if st.button(
                "Generate AI Analysis"
            ):

                with st.spinner(
                    "AI is generating investment insights..."
                ):

                    try:

                        ai_analysis = generate_ai_analysis(
                            info.get("longName"),
                            sector,
                            revenue_growth,
                            profit_margin,
                            pe_ratio
                        )

                        st.markdown(ai_analysis)

                    except Exception as ai_error:

                        if "429" in str(ai_error):

                            st.warning(
                                "Gemini API rate limit reached. Please try again shortly."
                            )

                        else:

                            st.error(
                                f"AI Analysis Error: {ai_error}"
                            )

            st.markdown(
                "## Latest Company News"
            )

            try:

                articles = get_company_news(
                    info.get("longName")
                )

                headline_text = ""

                for article in articles:

                    st.subheader(article["title"])

                    st.write(article["description"])

                    st.write(
                        f"Source: {article['source']['name']}"
                    )

                    st.markdown("---")

                    headline_text += (
                        article["title"] + "\n"
                    )

                st.markdown(
                    "## AI News Sentiment Analysis"
                )

                if st.button(
                    "Analyze News Sentiment"
                ):

                    with st.spinner(
                        "AI is analyzing market sentiment..."
                    ):

                        try:

                            sentiment_analysis = (
                                analyze_news_sentiment(
                                    headline_text
                                )
                            )

                            st.markdown(
                                sentiment_analysis
                            )

                        except Exception as sentiment_error:

                            if "429" in str(sentiment_error):

                                st.warning(
                                    "Gemini API rate limit reached. Please try again shortly."
                                )

                            else:

                                st.error(
                                    f"News Sentiment Error: {sentiment_error}"
                                )

            except Exception as news_error:

                st.warning(
                    f"News unavailable: {news_error}"
                )

            st.markdown("---")

            st.markdown(
                """
                <center>
                Built by Yash Goyal •
                AI Powered Equity Research Platform
                </center>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:

            if "429" in str(e):

                st.warning(
                    "API rate limit reached. Please wait a minute and try again."
                )

            else:

                st.error(f"Error: {e}")

