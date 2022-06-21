import requests
from bs4 import BeautifulSoup

for year in range(2017,2022): #
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
    res = requests.get(url,headers=headers )
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("img",attrs={'class':'thumb_img'})
    for idx,image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        image_res = requests.get(image_url,headers=headers)
        res.raise_for_status()

        with open("movie{}_{}.jpg".format(year,idx+1),"wb") as f:
            f.write(image_res.content)
        
        if idx >=4: # 상위 5개 영화 이미지만 다운로드
            break
