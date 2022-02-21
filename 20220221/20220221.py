# 병합 & 연결
import pandas as pd # pandas 모듈 호출
raw_data = {
'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
'test_score': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}
df_left = pd.DataFrame(raw_data, columns = ['subject_id', 'test_score'])

raw_data = {
            'subject_id': ['4', '5', '6', '7', '8'],
            'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
            'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
    }
df_right = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])

# 병합 subject_id 기준으로 합침
temp=pd.merge(left=df_left, right=df_right, how="inner", on="subject_id")
print(temp)

# how = 'left'     how='right'  how='outer'    NaN

#연결(concatenate) : 두 테이블을 그대로 붙임
#데이터의 스키마가 동일할 때 그대로 연결
#주로 세로로 데이터를 연결
#concat 함수 : 두 개의 서로 다른 테이블을 하나로 합침  -더 빠름
#append 함수 : 기존 테이블 하나에 다른 테이블을 붙임
import os
print(os.listdir('D:\\DATA_PY'))
pathlists = os.listdir('D:\\DATA_PY')
fullpath = os.path.join('D:\\DATA_PY', pathlists[0])
print(fullpath)

filenames = [os.path.join('D:\\DATA_PY', filename)
             for filename in os.listdir('D:\\DATA_PY') if 'sales' in filename]
print(filenames)

# pip install openpyxl

df_list= [pd.read_excel(filename) for filename in filenames]
for f in df_list:
    print(type(f), len(f))

df = pd.concat(df_list, axis=1) # 세로로 연결
print(f"len(df) = {len(df)}")
df.reset_index(drop=True)
print(df.head())
df.to_excel("D:/DATA_PY/totalmerge_1.xlsx", index=False)




