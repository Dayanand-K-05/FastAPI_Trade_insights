import requests

url = "http://127.0.0.1:8000/analyze/pharmaceuticals"
headers = {"x-api-key": "secret123"}

response = requests.get(url, headers=headers)
markdown = response.json()["report"]

# Save clean Markdown
with open("pharmaceuticals.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("✅ Markdown saved as technology.md")

