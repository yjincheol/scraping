from selenium import webdriver

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'Accept-Language': 'ko-KR,ko'}
url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Oct0121-Text_Search_BKWS-BKWS|ONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEFHIAmoPkBxQ1k1p-8tWWyKohe1X-rdZG5fe213RjMODCVw4qNgaURoCRzwQAvD_BwE"
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
movies = soup.find_all("div", attrs ={"class":"YMlj6b"})
print(movies)

# with open("move.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

# for movie in movies:
#     title = movie.find("span",attrs ={"class":"DdYX5"}).get_text()
#     print(title)