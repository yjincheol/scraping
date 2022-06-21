import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=' 
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

filename = "코스피 시가총액 1-200"
f = open(filename,'w',encoding='utf-8-sig', newline="")
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1,5): #상위 200
    res = requests.get(url+str(page),headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    # print(data_rows)
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns)<=1: #의미없는 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)
