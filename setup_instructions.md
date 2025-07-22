
# ⚙️ Setup & Run Instructions - FastAPI Market Analysis API

This document explains how to install dependencies, configure your environment, run the FastAPI app, and test the `/analyze/{sector}` endpoint.

---

## 📁 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/fastapi_trade_insights.git
cd fastapi_trade_insights
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
# For Linux/Mac
source env/bin/activate
# For Windows
env\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 🔐 Configure Environment Variables

Create a `.env` file in the project root with the following content:

```env
API_KEY=secret123
SERPAPI_API_KEY=your_serpapi_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## 🚀 Run the FastAPI App

```bash
uvicorn main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔑 API Key Authentication

All endpoints require an `x-api-key` header.

### Example with `curl`:

```bash
curl -X GET http://127.0.0.1:8000/analyze/technology -H "x-api-key: secret123"
```

---

## 🧪 Test Example with Python

```python
import requests

headers = {"x-api-key": "secret123"}
response = requests.get("http://127.0.0.1:8000/analyze/mobiles", headers=headers)

with open("mobiles_report.md", "w", encoding="utf-8") as f:
    f.write(response.json()["report"])
```

---

## 📊 Sample Sectors to Try

```http
/analyze/technology
/analyze/pharmaceuticals
/analyze/finance
/analyze/agriculture
/analyze/mobiles
```

---

## 🛠 Docs

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## ⚠️ Gemini API Quota Note

If you receive a 429 error, your Gemini account may have exceeded its **free tier usage**. To avoid this:

- Create a new Google Cloud project and generate a new Gemini API key.
- Reduce prompt size or frequency.

More info: [https://ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)
