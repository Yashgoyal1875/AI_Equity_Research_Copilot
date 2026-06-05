from newsapi import NewsApiClient
import streamlit as st


newsapi = NewsApiClient(
    api_key=st.secrets["NEWS_API_KEY"]
)


def get_company_news(company):

    try:

        news = newsapi.get_everything(
            q=f'"{company}"',
            language="en",
            sort_by="publishedAt",
            page_size=20
        )

        articles = news.get(
            "articles",
            []
        )

        filtered_articles = []

        for article in articles:

            title = article.get(
                "title",
                ""
            )

            description = article.get(
                "description",
                ""
            )

            if (
                title
                and title.isascii()
                and description
            ):
                filtered_articles.append(
                    article
                )

        return filtered_articles[:5]

    except Exception as e:

        st.error(
            f"News Error: {e}"
        )

        return []