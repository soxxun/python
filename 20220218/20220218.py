from pandas import Series,DataFrame
import pandas as pd
raw_data = {
    'name':['홍길동','철수','영희'],
    'age' : [42,52,62],
    "city" : ['서울특별시','부산광역시','경기도']
}
# df = DataFrame(raw_data,columns=['name','age','city'])
df = DataFrame(raw_data)
print(df)
df = DataFrame(raw_data,columns=['name','age'])
print(df)
# 데이터가 존재하지 않는 열을 추가하면 해당 열에는 NaN값을 추가
df = DataFrame(raw_data,columns=['name','age','address'])
print(df)
# pip install openpyxl
df = pd.read_excel("D:/DATA_PY/excel-comp-data.xlsx")  # https://github.com/bigdataleeky/python/tree/main/data
print(df)

print(df.head()) # default 5
print(df.head(1)) # default 5
print(df.head(3).T)
print(df.tail()) # default 5
# 원하는 데이터 추출하기  3개의 row
print(df.head(3))
print(df[:3])
print(df['name'])
print(df.columns)
print(df[['account','name']])
print( df[['account','name']][:2] )
#컬럼추출   데이터프레임[컬럼명]   or 데이터프레임.컬럼명
print(df.index)
print(df.account)

# 인덱스 변경
df.index = df.account
del df['account']
print(df.head())

# Question : index = 211829,109996  그리고 컬럼은 name street 정보만 추출
# hint print(df.loc[211829,'name'])
# answer
print(df.loc[ [211829,109996],['name','street'] ])

#index location  -> 슬라이싱을 이용할 수있음
print(df.iloc[:7])
print(df.iloc[5:7])
print("------------------------------")
print(df.columns)
print(df.iloc[:10,:3])

# index 재 할당(0부터) 여려개의 데이터프레임을 조합해서 하나의 데이터 프레임을 만들면
# 인덱스는 가져온 데이터의 인덱스로 표현
df_new =  df.reset_index()
print(df_new)

# drop  특정 열이나 행을 삭제한 객체를 반환
print(df_new.drop(1))
df_drop = df_new.drop(1)

#df_new 의 데이터가 drop
df_new.drop(1,inplace=True)

#열을 제거  axis =0(default)  -- row   axis = 1 -- col
print(df_new.drop("account",axis=1))
print(df_new.drop(["account","name"],axis=1))


