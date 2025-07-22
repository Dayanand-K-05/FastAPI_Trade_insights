# 📈 Trade Opportunities API

A FastAPI-based microservice that analyzes current market trends and provides markdown reports for various sectors in India.

---

## 🔧 Tech Stack

- **FastAPI** – Web Framework
- **Google Gemini API** – AI Report Generation (fallback used if quota exceeded)
- **SerpAPI** – Real-time news from Google
- **SlowAPI** – Rate limiting
- **.env** – API key management

---

## 🚀 Features

- ✅ `/analyze/{sector}` endpoint
- ✅ Fetches **live market news**
- ✅ Analyzes using **LLM (Gemini API)**
- ✅ Returns **Markdown-formatted** reports
- ✅ API Key Authentication (`x-api-key`)
- ✅ Rate limiting (5 requests/minute)
- ✅ Swagger API docs at `/docs`

---

## ⚠️ Gemini API Quota Note

This app uses the **Gemini API (Google Generative AI)** to analyze live market news and generate structured reports.

> ⚠️ **Note:** In case of Gemini API quota limits (e.g., daily/monthly limits exceeded), the application automatically **falls back** to a simulated markdown report.  
This ensures a stable user experience while demonstrating AI integration logic.

---


## 🧪 Example Usage

**Request:**

GET /analyze/technology
Header: x-api-key: secret123

**Response (truncated):**
```json
{
  "report": "# 📊 Market Analysis Report: Technology\n\n## Input News\n- headline 1\n- headline 2\n..."
}
