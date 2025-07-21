# import httpx

# async def fetch_market_news(sector: str) -> str:
#     try:
#         query = f"{sector} sector India news"
#         url = f"https://html.duckduckgo.com/html/?q={query}"

#         headers = {
#             "User-Agent": "Mozilla/5.0",
#         }

#         async with httpx.AsyncClient() as client:
#             response = await client.get(url, headers=headers)

#         if response.status_code != 200:
#             return f"Failed to fetch news: {response.status_code}"

#         # Basic scraping to pull headlines from DuckDuckGo HTML
#         from bs4 import BeautifulSoup
#         soup = BeautifulSoup(response.text, "html.parser")
#         results = soup.find_all("a", class_="result__a", limit=5)

#         headlines = "\n".join([f"- {r.get_text()}" for r in results])
#         return f"Recent news headlines about {sector} sector:\n{headlines}"

#     except Exception as e:
#         return f"Error fetching data: {str(e)}"
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

async def fetch_market_news(sector: str) -> str:
    try:
        params = {
            "q": f"{sector} sector India",
            "tbm": "nws",
            "api_key": SERPAPI_KEY,
        }
        url = "https://serpapi.com/search"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()

        data = response.json()
        news_results = data.get("news_results", [])

        if not news_results:
            return f"No news found for sector: {sector}"

        headlines = "\n".join(
            [f"- {article['title']} ({article['link']})" for article in news_results[:5]]
        )
        return f"Here are the latest news headlines for the {sector} sector in India:\n{headlines}"

    except Exception as e:
        return f"Error fetching news: {str(e)}"
