# > pip install selenium
# 크롬드라이버 적당한 곳에 다운받아서 풀기
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# chromedriver.exe 하고 브라우져하고 버전이 맞을것
# WebDriver 객체생성
wd = webdriver.Chrome('D:/web/chromedriver.exe')
#웹페이지 연결
coffeBean = 'https://www.coffeebeankorea.com/store/store.asp'
wd.get(coffeBean)
time.sleep(1) #웹페이지 연결을 위한 1초 대기
result = []
for i in range(1,500):
    try:
        # 자바스크립트함수를 이용해서 매장정보 팝업호출
        wd.execute_script("storePop2('1')")
        time.sleep(1) #스크립트 실행을 위한 1초 대기
        # 호출한팝업의 페이지 정보를 저장
        html = wd.page_source
        # html parser를 위한 BeautifulSoup 객체 생성
        soup =  BeautifulSoup(html,"html.parser")
        # print(soup.prettify())
        #매장 정보 추출
        store_name =  soup.select("div.store_txt>h2")
        store_name = store_name[0].string
        # print(store_name)
        # 매장 정보 출력
        store_info =  soup.select("div.store_txt > table.store_table > tbody > tr > td")
        # for data in store_info:
        #     print(data)
        # print(list(store_info[2]))
        # print(list(store_info[2])[0] )
        store_time = store_info[0].string
        store_address = list(store_info[2])[0]
        store_phone = store_info[3].string
        # print(f"매장명:{store_name} 영업시간:{store_time} 주소:{store_address} 전화번호:{store_phone}")
        result.append([store_name]+[store_time]+[store_address]+[store_phone])
    except:
        pass
wd.close()

df= pd.DataFrame(result, columns=('매장명','영업시간','주소','전화번호'))
df.to_csv('D:/coffeeBean.csv',encoding='cp949',mode='w',index=True)