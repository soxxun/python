import pandas as pd
# header None 엑셀에 있는 모든 데이터를 dataFrame으로 처리
# 생략하면 엑셀의 처음 한줄은 데이터프레임의 헤더정보로
df = pd.read_csv("D:/coffeeBean.csv",encoding='cp949')
print(df)
print(df['매장명'])

df = pd.read_csv("D:/coffeeBean.csv",encoding='cp949',header=None)
print(df)
print(df[1])