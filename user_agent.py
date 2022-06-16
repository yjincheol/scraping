import requests

url = 'http://naver.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status() # 오류가 있으면 프로그램 종료
# print("응답코드 :", res.status_code) # 200이면 정상

