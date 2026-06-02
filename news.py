
from newsapi import NewsApiClient
import streamlit as st

newsapi = NewsApiClient(
    api_key=st.secrets["NEWS_API_KEY"]
)

def get_company_news(company_name):

    news = newsapi.get_everything(
        q=company_name,
        language="en",
        sort_by="publishedAt",
        page_size=5
    )

    return news["articles"]
