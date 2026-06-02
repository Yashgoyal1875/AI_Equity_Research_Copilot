
import google.generativeai as genai


import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_ai_analysis(
    company_name,
    sector,
    revenue_growth,
    profit_margin,
    pe_ratio
):

    prompt = f"""

    Analyze this company like a professional equity research analyst.

    Company Name:
    {company_name}

    Sector:
    {sector}

    Revenue Growth:
    {revenue_growth:.2f}%

    Profit Margin:
    {profit_margin:.2f}%

    PE Ratio:
    {pe_ratio}

    Give detailed analysis on:

    1. Business strengths

    2. Key risks

    3. Growth outlook

    4. Investment summary

    5. Bull case

    6. Bear case

    """

    response = model.generate_content(
        prompt
    )

    return response.text


def analyze_news_sentiment(headlines):

    prompt = f"""

    Analyze the sentiment of these news headlines.

    Headlines:

    {headlines}

    Tell me:

    1. Overall sentiment

    2. Bullish or bearish outlook

    3. Major risks

    4. Key opportunities

    5. Short summary for investors

    """

    response = model.generate_content(
        prompt
    )

    return response.text
