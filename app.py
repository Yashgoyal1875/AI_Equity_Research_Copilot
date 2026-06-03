

from data import (
    get_company_data,
    get_stock_history,
    get_financial_statements
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
    • AI Investment Analysis  
    • Company News  
    • AI News Sentiment  
    """
)

stock = st.sidebar.text_input(
    "Enter Stock Symbol",
    value="IBM"
)

analyze = st.sidebar.button(
    "Analyze Stock"
)

if analyze:

    with st.spinner(
        "Analyzing company financials..."
    ):

        try:

            info = get_company_data(stock)

            company_name = info["Name"]

            sector = info["Sector"]

            market_cap = float(
                info["MarketCapitalization"]
            )

            pe_ratio = float(
                info["PERatio"]
            )

            st.header(company_name)

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Business Sector",
                sector
            )

            col2.metric(
                "Market Capitalization",
                f"{market_cap / 1_000_000_000:.2f} B"
            )

            col3.metric(
                "PE Ratio",
                round(pe_ratio, 2)
            )

            data = get_stock_history(stock)

            create_stock_chart(data)

            st.markdown(
                "## AI Investment Analysis"
            )

            if st.button(
                "Generate AI Analysis"
            ):

                with st.spinner(
                    "Generating AI insights..."
                ):

                    ai_analysis = (
                        generate_ai_analysis(
                            company_name,
                            sector,
                            0,
                            0,
                            pe_ratio
                        )
                    )

                    st.markdown(ai_analysis)

            st.markdown(
                "## Latest Company News"
            )

            articles = get_company_news(
                company_name
            )

            headlines = ""

            for article in articles:

                st.subheader(
                    article["title"]
                )

                st.write(
                    article["description"]
                )

                st.write(
                    f"Source: {article['source']['name']}"
                )

                st.markdown("---")

                headlines += (
                    article["title"] + "\n"
                )

            st.markdown(
                "## AI News Sentiment"
            )

            if st.button(
                "Analyze News Sentiment"
            ):

                with st.spinner(
                    "Analyzing news sentiment..."
                ):

                    sentiment = (
                        analyze_news_sentiment(
                            headlines
                        )
                    )

                    st.markdown(sentiment)

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

            st.error(f"Error: {e}")
