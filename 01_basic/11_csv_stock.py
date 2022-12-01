import csv

import requests
from bs4 import BeautifulSoup

filename = "01_basic/시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?&page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    # with open("01_basic/naverstock.html", "w", encoding="utf8") as f:
    #     f.write(res.text)

    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) < 2:  # 의미 없는 데이터는 스킵
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)
