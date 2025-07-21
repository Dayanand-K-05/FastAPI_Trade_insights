from fastapi import FastAPI, HTTPException, Request, Header, Depends
from dotenv import load_dotenv
import os

from slowapi.extension import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler

from analysis import generate_analysis_report
from fetch_data import fetch_market_news

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY", "secret123")

# Initialize FastAPI app
app = FastAPI()

# Configure limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# API key verification
async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# ✅ Use shared_limit as a decorator
@limiter.shared_limit("5/minute", scope="analyze")
@app.get("/analyze/{sector}")
async def analyze_sector(
    request: Request,
    sector: str,
    _: str = Depends(verify_api_key)
):
    try:
        content = await fetch_market_news(sector)
        markdown_report = await generate_analysis_report(sector, content)
        return {"report": markdown_report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
