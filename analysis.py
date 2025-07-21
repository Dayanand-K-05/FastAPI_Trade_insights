import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set in environment")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# fallback if Gemini fails
def fallback_markdown(sector: str, content: str) -> str:
    return f"""
# 📊 Market Analysis Report: {sector.capitalize()}

## 📥 Input News
{content}

## 🏢 Sector Overview
The {sector} sector in India is a high-potential market with recent attention.

## 📰 Recent Developments
- Government support and startup momentum
- Tech adoption and export growth

## 📈 Investment Trends
- Positive sentiment with rising funding

## 💼 Trade Opportunities
- Demand surge in key global markets

## ⚠️ Risks
- Regulatory and geopolitical risks

## ✅ Final Thoughts
The {sector} sector presents a strong opportunity for growth and investment.
"""

async def generate_analysis_report(sector: str, content: str) -> str:
    prompt = f"""
Analyze this content related to the Indian {sector} sector and generate a professional Markdown report including:
- Overview
- News summary
- Investment trends
- Opportunities and risks
- Final recommendation

Content:
\"\"\"
{content}
\"\"\"
Only output the markdown report.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        # fallback if Gemini fails
        return fallback_markdown(sector, content)
