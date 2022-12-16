# p = re.compile("원하는 형태")
# 1. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 2. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 3. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (0) | face (X)

import re


p = re.compile("ca.e")


def print_match(_m):
    if _m:
        print("m.string:", _m.string)  # 입력받은 문자열 반환
        print("m.group():", _m.group())  # 일치하는 문자열 반환
        print("m.start():", _m.start())  # 일치하는 문자열의 시작 index
        print("m.end():", _m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", _m.span())  # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")


m = p.match("sccarefhcafei")
print_match(m)

m = p.search("sccarefhcafei")
print_match(m)

lst = p.findall("sccarefhcafei")
print(lst)
