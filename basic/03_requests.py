import requests

res = requests.get("http://www.google.co.kr", timeout=5)
# res = requests.get("http://www.nadocoding.tistory.com")
res.raise_for_status()
# print("응답코드 :", res.status_code) # 200 이면 정상
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

print(len(res.text))

with open("01_basic/mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
