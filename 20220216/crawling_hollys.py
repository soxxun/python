from bs4 import BeautifulSoup as bs
import urllib.request as request

def getStoresHolly():
    result = []
    for pagenum in range(1,53+1):
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={pagenum}&sido=&gugun=&store="
        html=request.urlopen(url)
        soup =  bs(html,"html.parser")
        tag_tobody= soup.find('tbody')
        for s in  tag_tobody.find_all('tr'):
            s_td = s.find_all('td')
            # print(s_td)
            s_reg= s_td[0].string
            s_name = s_td[1].string
            s_state = s_td[2].string
            s_addr = s_td[3].string
            s_phone = s_td[5].string
            result.append([s_reg]+[s_name]+[s_state]+[s_addr]+[s_phone])
    # print(len(result))
    return result
getStoresHolly()
# for store in result:
#     print(store)