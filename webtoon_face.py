import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=641253'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
res = requests.get(url,headers=headers )
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 만화 제목, 링크 가져오기
cartoons = soup.find_all('td', attrs={'class':'title'})
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a['href']
    print(title, link)

# 평점 구하기
tot_rates = 0
cartoons_rating = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons_rating:
    rate = cartoon.find('strong').get_text()
    print(rate)
    tot_rates+=float(rate)
print('전체점수 : ', tot_rates)
print('평균점수 : ', tot_rates/len(cartoons_rating))