from data import (
get_company_data,
get_stock_history
)

from charts import create_stock_chart

from analysis import (
generate_ai_analysis,
analyze_news_sentiment
)

from news import get_company_news

import streamlit as st
import traceback

st.set_page_config(
page_title="AI Equity Research Copilot",
layout="wide"
)

st.markdown(
""" <h1 style='text-align: center; color: #00FFAA;'>
AI Equity Research Copilot </h1>

```
<h4 style='text-align: center; color: gray;'>
AI Powered Financial Intelligence Platform
</h4>
""",
unsafe_allow_html=True
```

)

st.sidebar.markdown(
"## Powered by Groq AI"
)

st.sidebar.markdown("---")

st.sidebar.markdown(
"""
## Dashboard Sections

```
• Stock Chart
• AI Investment Analysis
• Company News
• AI News Sentiment
"""
```

)

stock = st.sidebar.text_input(
"Enter Stock Symbol",
value="IBM"
)

if "analyzed" not in st.session_state:
st.session_state.analyzed = False

if st.sidebar.button("Analyze Stock"):
st.session_state.analyzed = True

if st.session_state.analyzed:

```
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
        "Sector",
        sector
    )

    col2.metric(
        "Market Cap",
        f"{market_cap / 1_000_000_000:.2f} B"
    )

    col3.metric(
        "PE Ratio",
        round(pe_ratio, 2)
    )

    st.markdown("---")

    st.subheader(
        "1 Year Stock Price Trend"
    )

    data = get_stock_history(stock)

    create_stock_chart(data)

    st.markdown("---")

    st.subheader(
        "AI Investment Analysis"
    )

    if st.button(
        "Generate AI Analysis"
    ):

        with st.spinner(
            "Generating AI analysis..."
        ):

            ai_analysis = generate_ai_analysis(
                company_name,
                sector,
                market_cap,
                0,
                pe_ratio
            )

            st.markdown(ai_analysis)

    st.markdown("---")

    st.subheader(
        "Latest Company News"
    )

    articles = get_company_news(
        company_name
    )

    headlines = ""

    for article in articles[:5]:

        st.markdown(
            f"### {article['title']}"
        )

        st.write(
            article["description"]
        )

        st.caption(
            f"Source: {article['source']['name']}"
        )

        st.markdown("---")

        headlines += (
            article["title"] + "\n"
        )

    st.subheader(
        "AI News Sentiment"
    )

    if st.button(
        "Analyze News Sentiment"
    ):

        with st.spinner(
            "Analyzing sentiment..."
        ):

            sentiment = analyze_news_sentiment(
                headlines
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
