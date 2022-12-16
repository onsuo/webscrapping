"""
Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑하는 프로그램을 만드시오

[조회 조건]
1. https://daum.net 접속
2. '송파 헬리오시티' 검색
3. 다음 부동산 부분에 나오는 결과 정보

[출력 결과]
=========== 매물 1 ===========
거래 : 매매
면적 : 84/59 (공급/전용)
가격 : 165,000 (만원)
동 : 214동
층 : 고/23
=========== 매물 2 ===========
    ...

[주의사항]
- 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능



* 부동산 거래 기록으로 변경

[조회 조건]
1. https://realty.daum.net/ 접속
2. '송파 헬리오시티' 검색
3. 실거래가 정보

[출력 결과]
=========== 매물 1 ===========
거래일 : 2022.12.14
거래 : 매매
가격 : 17억
타입 : 107J1, 107J2
층 : 23
=========== 매물 2 ===========
    ...
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
)
options.add_argument("lang=ko_KR")

browser = webdriver.Chrome("chromedriver", options=options)
browser.maximize_window()

url = "https://realty.daum.net/home/apt/danjis/38487"
browser.get(url)

for i in range(3):
    (
        browser.find_element(By.CLASS_NAME, "sc-fHYyUA.lhwDqs")
        .find_element(By.XPATH, "//*[text()='더보기']")
        .click()
    )

soup = BeautifulSoup(browser.page_source, "lxml")

houses = soup.find_all(
    "div",
    attrs={
        "class": "css-1dbjc4n r-1awozwy r-p9m3gb r-17leim2 r-1sxrcry r-13awgt0 r-1mlwlqe r-18u37iz r-17j37da r-lgpkq r-qi0n3 r-c9eks5 r-k5i03q"
    },
)

for i, house in enumerate(houses):
    columns = house.find_all("div", attrs={"class": "css-1563yu1"})

    date = columns[0].get_text().replace(" ", "")

    form = columns[1].get_text()
    price = columns[2].get_text()

    size = columns[3].get_text() + " m²"

    floor = columns[4].get_text()
    if floor[0] == "외":
        floor = columns[5].get_text()

    print(f"=========== 매물 {i + 1} ===========")
    print(f"거래일 : {date}")
    print(f"거래 : {form}")
    print(f"가격 : {price}")
    print(f"타입 : {size}")
    print(f"층 : {floor}")

browser.quit()
