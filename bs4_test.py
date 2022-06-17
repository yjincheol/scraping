#pip install beautifulsoup4
#pip install lxml

import requests
from bs4 import BeautifulSoup

url = 'http://comic.naver.com/webtoon/weekday'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title) #<title>네이버 웹툰 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
# print(soup.title.get_text()) #네이버 웹툰 > 요일별  웹툰 > 전체웹툰
# print(soup.a.attrs) #{'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}
# print(soup.a['href']) #menu
# print(soup.find('a', attrs={'class': 'Nbtn_upload'})) #<a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
# print(soup.find('li',attrs={'class': 'rank01'}))
# rank1 = soup.find('li',attrs={'class': 'rank01'})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling('li')
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())
# print(rank1.find_next_siblings('li'))

# 네이버 웹툰 전체목록 가져오기
cartoons = soup.find_all('a',attrs={'class': 'title'})

for cartoon in cartoons:
    print(cartoon.get_text())