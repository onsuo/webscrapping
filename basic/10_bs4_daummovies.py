import requests
from bs4 import BeautifulSoup

# f = open("01_basic/movierank.txt", "w", encoding="utf8")

for year in range(2015, 2022):
    url = f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={year}+관객순위"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"
    }

    res = requests.get(url, headers=headers, timeout=5)
    res.raise_for_status()

    # with open("01_basic/daummovie.html", "w", encoding="utf8") as f:
    #     f.write(res.text)

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for i, image in enumerate(images):
        if i > 4:
            break

        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        print(image_url)
        # f.write(image_url + "\n")

        image_res = requests.get(url, headers=headers, timeout=5)
        image_res.raise_for_status()

        with open(f"01_basic/movie_{year}_{i + 1}.jpg", "wb") as f:
            f.write(image_res.content)

# f.close()
