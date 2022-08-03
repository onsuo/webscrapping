import re
import json

import requests
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all"
params = {
    "frm":"NVSHATC",
    "origQuery":"노트북",
    "pagingIndex":"1",
    "pagingSize":"40",
    "productSet":"total",
    "query":"노트북",
    "sort":"rel",
    "viewType":"list"
}
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"}
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
    item_name = item["item"]["productTitle"]
    item_price = item["item"]["price"] + "원"
    product_info = ( item_name, item_price )
    print(product_info)
