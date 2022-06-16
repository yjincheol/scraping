# import re

#1. p = re.compile("원하는 형태")
#2. m = re.match("비교할 문자열") # 주어진 문자열의 처음부터 일치하는지 확인
#1. m = re.search("비교할 문자열") # 주어진 문자열 중에 일치하는게 있는지 학인
#1. lst = re.findall("비교할 문자열") # 일치하는 모든것을 리스트로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case / caffe(x)
# ^ (^de) : 문자열 시작 -> desk, destination / fade(x)
# $ (se$) : 문자열 끝 -> case, base / face(x)