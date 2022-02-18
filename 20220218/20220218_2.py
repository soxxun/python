#그룹별 집계
# groupby : 동일한 객체를 가진 데이터만 따로 뽑아 기술통계(최대,최소,평균,합,갯수) 데이터를 추출
# 엑셀의 피봇페이블 기능과 유사
#예  같은 성별을 가진 학생들의 평균점수
# 50점 이상을 받은 학생의 수

# 로직은 아래 3단계를 거친다
# 분할
# 적용
# 결합

# 연습용 데이터 생성
import pandas as pd
import numpy as np

data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings','kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(data)
print(df.head())

teampointsum= df.groupby(by='Team')['Points'].sum()
print(teampointsum)
print(teampointsum.index)
# print(teampointsum.unstack())  index must be a MultiIndex to unstack

teamyear_points_sum =  df.groupby(by=['Team','Year'])['Points'].sum()
print(teamyear_points_sum)
print(teamyear_points_sum.index)


# Team에대한 컬럼 데이터 추출
print("-------------------------")
print(df['Team'])
print(df.index)
print(df[3:6])

print("teamyear_points_sum -------------------------")
# teamyear_points_sum
print(teamyear_points_sum["Devils":"Kings"])

print(teamyear_points_sum)
print("---------------------------------------------")
print(teamyear_points_sum.unstack())

# 분할->적용->상태
# 분할까지만 적용한 상태에서
grouped = df.groupby(by='Team')
# 해당 키값을 기준으로 데이터의 상태를 확인
print(grouped.get_group("Kings"))

#agg(aggregation) 함수  모든컬럼에 대해서..
print(grouped.agg(min))  # 최소
print(grouped.agg(np.mean)) # 평균

# 변환(transformation) -- 조사...
# 키값별로 요약된 정보가 아닌 개별 데이터 변환지원
# 적용시점에서는 그릅화된 상태의 값으로 적용
print("grouped.agg(max)---------------------------------")
print(grouped.agg(max))  # 최대
print("---------------------------------")
print(grouped.transform(max))
print(df)
print("----------------------------------")
score = lambda x:(x - x.mean())/x.std()
print(grouped.transform(score))

# 필터  : 특정 조건으로 데이터를 추출
# filter
temp = df.groupby("Team").filter(
    lambda x:x['Points'].max()>850
)
print(temp)

print(df.groupby('Team')["Points"].max())


# key word
# groupby / agg / transform

# 깃에 있는 sales-feb-2014.xlsx 을 읽어서
# 고객별 구매수량

df=pd.read_excel("d:/DATA_PY/sales-feb-2014.xlsx")
print(df.head())
print(df.columns)
df.sum =  df.groupby(['name'])['quantity'].sum()
print(df.sum)

# 고객별 구매금액
# hint 수량*단위금액의 합  ext price
totalsum = lambda x:x['quantity']*x['unit price']
print(df[['quantity','unit price']].apply(totalsum,axis=1))

df['totalPrice'] = df[['quantity','unit price']].apply(totalsum,axis=1)
print(df.head())

print(df.groupby(['name'])['totalPrice'].sum())
# 데이터 추가  year month day
# 고객별 연도별 월별 구매금액

print(df['date'][0][:10])

# data = {
#     'a':[1,2,3],
#     'b':[4,5,6]
# }
# df = pd.DataFrame(data)
# print(df)
# df['c'] = 0
# print(df)


#판다스 슬라이스에대서 셈플 만듣고 제공 - 이규영