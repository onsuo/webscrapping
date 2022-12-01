import time

from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
)
options.add_argument("lang=ko_KR")
options.headless = True

browser = webdriver.Chrome("chromedriver", options=options)
browser.maximize_window()

url = "https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&cat_id=&frm=NVSHATC"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920 x 1080

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 2초에 한번씩 스크롤 내림
interval = 0.5

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        print("스크롤 완료")
        break
    prev_height = curr_height

soup = BeautifulSoup(browser.page_source, "lxml")

products = soup.find_all(
    "li", attrs={"class": ["basicList_item__0T9JD", "basicList_item__0T9JD ad"]}
)
print(f"검색된 상품 개수 : {len(products)}")

for product in products:
    title = product.find("div", attrs={"class": "basicList_title__VfX3c"})

    # 가격
    price = product.find("span", attrs={"class": "price_num__S2p_v"}).get_text()

    if int(price.rstrip("원").replace(",", "")) >= 1000000:
        # print(title.get_text(), "  <1,000,000원 이상인 노트북 제외>")
        # print("-" * 120)
        continue

    # 링크
    link = title.find("a", attrs={"class": "basicList_link__JLQJf"})["href"]

    print(f"제목 : {title.get_text()}")
    print(f"가격 : {price}")
    print(f"링크 : {link}")
    print("-" * 120)

browser.quit()
