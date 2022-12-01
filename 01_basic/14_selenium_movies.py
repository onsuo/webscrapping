import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies?hl=ko&gl=US"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8",
}
res = requests.get(url=url, headers=headers, timeout=5)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open("movies.html", "w", encoding="utf8") as f:
    f.write(res.text)

movies = soup.find_all(
    "div", attrs={"class": "VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  QafiQ"}
)
print(len(movies))  # 0

# 동적 웹페이지 : beautifulsoup 으로는 스크래핑 불가능
# scripts 부분의 탐색은 09_bs4_navershopping.py 에서 확인 가능
