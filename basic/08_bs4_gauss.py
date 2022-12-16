import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url, timeout=5)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons1 = soup.find_all("td", attrs={"class": "title"})
title = cartoons1[0].a.get_text()
link = cartoons1[0].a["href"]
print(title)
print("https://comic.naver.com" + link)

# 만화 제목과 링크 가져오기
for cartoon in cartoons1:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)

# 평점 구하기
total_rates = 0
cartoons2 = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons2:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 :", total_rates)
print("평균 점수 :", total_rates / len(cartoons2))
