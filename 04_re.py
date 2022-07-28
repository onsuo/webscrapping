import re

# 번호판 abcd, book, desk
# ca?e

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (0) | face (X)

def print_match(_m):
    if _m:
        print(_m.group()) # 매치되지 않으면 에러가 발생
    else:
        print("매칭되지 않음")

m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
