import requests


url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"
}

res = requests.get(url, headers=headers, timeout=5)
res.raise_for_status()

with open("01_basic/nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
