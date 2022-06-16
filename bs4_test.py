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
print(soup.find('a', attrs={'class': 'Nbtn_upload'})) #<a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
