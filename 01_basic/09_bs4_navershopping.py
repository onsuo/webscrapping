import re
import json
import requests
from bs4 import BeautifulSoup

# f = open("01_basic/items.txt", "w", encoding="utf8")
item_count = 0

url = "https://search.shopping.naver.com/search/all"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"}

for i in range(1, 11):
    params = {
        "pagingIndex":str(i),
        "pagingSize":"40",
        "frm":"NVSHATC",
        "origQuery":"노트북",
        "productSet":"total",
        "query":"노트북",
        "sort":"rel",
        "viewType":"list"
    }
    res = requests.get(url, params=params, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    full_dict = soup.find("script", attrs={"id":"__NEXT_DATA__"})

    # with open("01_basic/navershopping.html", "w", encoding="utf8") as f:
    #     f.write(items.get_text())
    # with open("01_basic/script.json", "w", encoding="utf8") as f:
    #     f.write(items.get_text())

    result_dict = json.loads(full_dict.get_text())

    items = result_dict["props"]["pageProps"]["initialState"]["products"]["list"]

    for item in items:
        # 광고 상품 제외
        try:
            item["item"]["adId"]
        except KeyError:
            pass
        else:
            # print("  <광고 상품 제외됨.>")
            continue

        item_name = item["item"]["productTitle"]
        # 애플 상품 제외
        if "Apple" in item_name:
            # print("  <Apple 상품 제외됨.>")
            continue

        item_price = int(item["item"]["price"])

        # 리뷰 200개 이상, 평점 4.9 이상인 상품만 선택
        if item["item"]["scoreInfo"]:
            item_score = float(item["item"]["scoreInfo"])
        else:
            # print("  <평점 없는 상품 제외됨.>")
            continue

        if item["item"]["reviewCount"]:
            item_review_count = int(item["item"]["reviewCount"])
        else:
            # print("  <리뷰 없는 상품 제외됨.>")
            continue

        item_link = item["item"]["crUrl"]

        if item_score >= 4.9 and item_review_count >= 200:
            # f.write(f"{item_name} | {item_price:,}원 | {item_score:.2f}점 ({item_review_count}개)\n링크: {item_link}\n")
            print(f"{item_name} | {item_price:,}원 | {item_score:.2f}점 ({item_review_count}개)\n링크: {item_link}\n")
            item_count += 1

# f.close()
print(f"검색된 상품 개수 : {item_count}")
