
# https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0
# 상위 200개까지 정보 저장하기 --> 약 4페이지

import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
filename = '시가총액_1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') # newline = 엔터 없이 데이터 삽입
# 엑셀 파일에서의 한글 오류  --> utf-8-sig
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)
# tap으로 구분한 데이터들이 리스트로 변환되어 'title' 변수에 저장됨 --> ['N', '종목명', '현재가', ...]

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    data_rows = soup.find('table', {'class':'type_2'}).find('tbody').find_all('tr')

    for row in data_rows:
        # 각 td들이 가지고 있는 텍스트 정보 저장하기
        columns = row.find_all('td')
        # 공백 제거 (tr이 하나 또는 그 이하의 td를 가지는 데이터는 skip)
        if len(columns) <= 1: # 의미 없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        # 리스트 형태로 넣어 주기 (단, 'data' 변수에 담긴 데이터가 이미 리스트 형태이므로 변수명만 넣어주면 됨)
        writer.writerow(data)






