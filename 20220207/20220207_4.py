# 외부모듈 설치
# python -m pip install --upgrade pip
# pip install beautifulsoup4

from urllib import request
from bs4 import BeautifulSoup

# https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
# target =  request.urlopen("https://www.daum.net/")
# print(target.read())

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?"
target = request.urlopen(url)
soup = BeautifulSoup(target,"html.parser")
# soup.select("location") # 태그정보 찾기
with open("weather.txt","a") as f:
    for lo in soup.select("location"):
        data = "\n".join([f"날자:{lo.select_one('tmEf').string}",
                   f"도시:{lo.select_one('city').string}",
                   f"날씨:{lo.select_one('wf').string}",
                   f"최저기온:{lo.select_one('tmn').string}",
                   f"최고기온:{lo.select_one('tmx').string}",
                   "--------------------------------------\n"])
        print(data)
        f.write(data)

        # print(f'날자 : {lo.select_one("tmEf").string}')
        # print(f'도시 : {lo.select_one("city").string}')
        # print(f'날씨 : {lo.select_one("wf").string}')
        # print(f'최저기온 : {lo.select_one("tmn").string}')
        # print(f'최고기온 : {lo.select_one("tmx").string}')
        # print("-------------------------------------------")
