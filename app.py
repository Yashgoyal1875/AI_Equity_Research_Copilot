from data import (
    get_company_data,
    get_stock_history
)

from charts import (
    create_stock_chart
)

from analysis import (
    generate_ai_analysis,
    analyze_news_sentiment
)

from news import (
    get_company_news
)

import streamlit as st
import traceback


st.set_page_config(
    page_title="AI Equity Research Copilot",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align:center;color:#00FFAA'>
    AI Equity Research Copilot
    </h1>

    <h4 style='text-align:center;color:gray'>
    AI Powered Financial Intelligence Platform
    </h4>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "## Powered by Groq AI"
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ## Dashboard Sections

    • Stock Chart

    • AI Investment Analysis

    • Company News

    • AI News Sentiment
    """
)

stock = st.sidebar.text_input(
    "Enter Stock Symbol",
    value="IBM"
)

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

if st.sidebar.button(
    "Analyze Stock"
):
    st.session_state.analyzed = True

if st.session_state.analyzed:

    try:

        info = get_company_data(stock)

        company_name = info.get(
            "Name",
            stock
        )

        sector = info.get(
            "Sector",
            "Unknown"
        )

        market_cap = info.get(
            "MarketCapitalization",
            0
        )

        pe_ratio = info.get(
            "PERatio",
            0
        )

        try:
            market_cap = float(
                market_cap
            )
        except:
            market_cap = 0

        try:
            pe_ratio = float(
                pe_ratio
            )
        except:
            pe_ratio = 0

        st.header(
            company_name
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Sector",
            sector
        )

        if market_cap > 0:

            market_cap_display = (
                f"{market_cap / 1_000_000_000:.2f} B"
            )

        else:

            market_cap_display = "N/A"

        col2.metric(
            "Market Cap",
            market_cap_display
        )

        col3.metric(
            "PE Ratio",
            round(pe_ratio, 2)
            if pe_ratio > 0
            else "N/A"
        )

        st.markdown("---")

        st.subheader(
            "1 Year Stock Price Trend"
        )

        data = get_stock_history(
            stock
        )

        create_stock_chart(
            data
        )

        st.markdown("---")

        st.subheader(
            "AI Investment Analysis"
        )

        if st.button(
            "Generate AI Analysis"
        ):

            with st.spinner(
                "Generating AI Analysis..."
            ):

                ai_analysis = (
                    generate_ai_analysis(
                        company_name,
                        sector,
                        market_cap,
                        0,
                        pe_ratio
                    )
                )

                st.markdown(
                    ai_analysis
                )

        st.markdown("---")

        st.subheader(
            "Latest Company News"
        )

        articles = (
            get_company_news(
                company_name
            )
        )

        headlines = ""

        if not articles:

            st.warning(
                "No news available."
            )

        else:

            for article in articles[:5]:

                st.markdown(
                    f"### {article.get('title', 'No Title')}"
                )

                st.write(
                    article.get(
                        "description",
                        "No description available."
                    )
                )

                source = article.get(
                    "source",
                    {}
                )

                st.caption(
                    f"Source: {source.get('name', 'Unknown')}"
                )

                st.markdown(
                    "---"
                )

                headlines += (
                    article.get(
                        "title",
                        ""
                    )
                    + "\n"
                )

        st.subheader(
            "AI News Sentiment"
        )

        if st.button(
            "Analyze News Sentiment"
        ):

            if headlines.strip() == "":

                st.warning(
                    "No headlines available for sentiment analysis."
                )

            else:

                with st.spinner(
                    "Analyzing News Sentiment..."
                ):

                    sentiment = (
                        analyze_news_sentiment(
                            headlines
                        )
                    )

                    st.markdown(
                        sentiment
                    )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

        st.code(
            traceback.format_exc()
        )