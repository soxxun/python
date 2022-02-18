# pandas
# 데이터 분석 라이브러리
# 넘파이를 효율적으로 사용하기 위해서 인덱싱, 연산, 전처리등의 함수를 제공
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
list_data = [1,2,1,4,2]
list_name = ['a','b','c','d','e']
s = Series(data = list_data,index=list_name)
print("시리즈출력")
print(s)
print("시리즈에서 인덱스정보")
print(s.index)
print("시리즈에서 값")
print(s.values)
print("시리즈에서 값의 빈도수")
print(s.value_counts())
print(s.dtype)
print(s.name)
s.name = 'number'
s.index.name = 'id'
print(s)
################################
dic_data = {'a':1,'b':2,'c':3}
s = Series(data=dic_data,dtype=np.float32, name="example_data")
print(s)

# 데이터 프레임
# 데이터 테이블 전체를 지칭하는 객체
# 넘파이 배열의 특성을 가짐
# 인덱싱 : 열과 행 각각 사용하여 하나의 데이터에 접근

data = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
df = pd.read_csv(data,header=None)
df = pd.DataFrame(df)
print(df.dtypes)

pd = pd.read_csv('D:/coffeeBean.csv',encoding='cp949')
print(pd)

