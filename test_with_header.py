import requests

url = "http://127.0.0.1:8000/analyze/technology"
headers = {
    "x-api-key": "secret123"
}

response = requests.get(url, headers=headers)
print(response.json())
