import requests
from bs4 import BeautifulSoup

def getTotalPages():
    page = 1
    last_page = 0

    while True:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
        url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=LG%20CNS%20%EB%8C%80%ED%95%9C%ED%95%AD%EA%B3%B5&sort=2&photo=0&field=0&pd=3&ds=2019.01.01&de=2019.12.31&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20190101to20191231,a:all&start={str(page)}'
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')


        if soup.select_one('다음') == None: # 다음음 없다면
           last_page += page
            break
        page = page + 1

    return last_page

getTotalPages()

'''
for i in range():
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=LG%20CNS%20%EB%8C%80%ED%95%9C%ED%95%AD%EA%B3%B5&sort=2&photo=0&field=0&pd=3&ds=2019.01.01&de=2019.12.31&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20190101to20191231,a:all&start={i}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    a = soup.find('p', {'class':'section-1'})
    print(a)
'''
# items = soup.find_all('td', attrs={'cl