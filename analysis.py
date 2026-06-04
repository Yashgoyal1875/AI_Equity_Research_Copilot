from groq import Groq
import streamlit as st


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def generate_ai_analysis(
    company_name,
    sector,
    market_cap,
    revenue,
    pe_ratio
):

    try:

        prompt = f"""
        Analyze this company.

        Company: {company_name}

        Sector: {sector}

        Market Cap: {market_cap}

        PE Ratio: {pe_ratio}

        Give:

        1. Business Overview

        2. Strengths

        3. Risks

        4. Investment Outlook
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI Analysis Error: {str(e)}"


def analyze_news_sentiment(headlines):

    try:

        prompt = f"""
        Analyze these news headlines.

        {headlines}

        Give:

        1. Overall Sentiment

        2. Positive Factors

        3. Negative Factors

        4. Likely Market Impact
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"News Sentiment Error: {str(e)}"