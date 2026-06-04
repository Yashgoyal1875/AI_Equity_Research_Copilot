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
Analyze this company as an equity research analyst.

Company Name: {company_name}
Sector: {sector}
Market Cap: {market_cap}
PE Ratio: {pe_ratio}

Give:

1. Business Overview
2. Strengths
3. Risks
4. Investment Outlook
5. Investment Recommendation
"""

        response = client.chat.completions.create(
          model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=1000
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI Analysis Error: {str(e)}"


def analyze_news_sentiment(headlines):
    try:

        prompt = f"""
Analyze the sentiment of these news headlines.

Headlines:

{headlines}

Give:

1. Overall Sentiment
2. Positive Factors
3. Negative Factors
4. Potential Market Impact
5. Investment Takeaway
"""

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=1000
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"News Sentiment Error: {str(e)}"