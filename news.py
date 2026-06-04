from newsapi import NewsApiClient
import streamlit as st


newsapi = NewsApiClient(
    api_key=st.secrets["NEWS_API_KEY"]
)


def get_company_news(company):

    try:

        news = newsapi.get_everything(
            q=company,
            language="en",
            page_size=10
        )

        return news["articles"]

    except Exception:

        return []