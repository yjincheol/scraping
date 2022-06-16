#pip install requests   
import requests

url = 'http://naver.com'
# url = 'http://nadocoding.tistory.com'
res = requests.get(url)
res.raise_for_status() # 오류가 있으면 프로그램 종료
# print("응답코드 :", res.status_code) # 200이면 정상

