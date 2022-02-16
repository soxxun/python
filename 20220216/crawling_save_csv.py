import pandas as pd
import crawling_hollys as ch
def main():
    result = ch.getStoresHolly()
    df= pd.DataFrame(result, columns=('지역','매장명','현황','주소','전화번호'))
    df.to_csv("D:/holly_coffe_stores.csv",encoding='cp949',mode='w',index=True)

if __name__ == '__main__':
    main()