## T1-19. 시계열 데이터3 (https://www.kaggle.com/code/agileteam/py-t1-19-3-expected-question)
# 주어진 데이터에서 2022년 월별 Sales 합계 중 가장 큰 금액과 2023년 월별 Sales 합계 중 가장 큰 금액의 차이를 절대값으로 구하시오.
# 단 Events컬럼이 '1'인경우 80%의 Salse값만 반영

import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic2.csv')
print(df.head(4))
print(df.info())

df['year'] = pd.to_datetime(df['Date']).dt.year
df['month'] = pd.to_datetime(df['Date']).dt.month
print(df.head(5))

def event_sales(x):
    if x['Events'] == 1:
        x['Sales2'] = x['Sales']*0.8
    else:
        x['Sales2'] = x['Sales']
    
    return x

df = df.apply(lambda x: event_sales(x), axis=1) # 컬럼에 적용
# print(df.head(5))
# df = df.groupby(['year', 'month'])['Sales2'].sum() # 전체 테이블로 확인
df1 = df[df['year'] == 2022]
df2 = df[df['year'] == 2023]

sales1 = df1.groupby('month')['Sales2'].sum().max()
sales2 = df2.groupby('month')['Sales2'].sum().max()
print(int(round(abs(sales1 - sales2), 0)))

## T1-20. 데이터 병합 (https://www.kaggle.com/code/agileteam/py-t1-20-expected-question)
# 고객과 잘 맞는 타입 추천 / basic1 데이터와 basic3 데이터를 'f4'값을 기준으로 병합

df1 = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
print(df1.head(4))

df2 = pd.read_csv('../input/bigdatacertificationkr/basic3.csv')
print(df2.head(4))

df3 = pd.merge(df1, df2, on = 'f4')
print(df3.head(5))

# 병합한 데이터에서 r2결측치를 제거한 다음, 앞에서 부터 20개 데이터를 선택하고 'f2'컬럼 합을 구하시오
print(df3['r2'].isnull().sum())
df3 = df3.dropna(subset=['r2'])
df3= df3.reset_index()
df3.drop('index', axis=1, inplace=True)
print(df3.head(4))
print(df3[:20]['f2'].sum()) # => 답이 15가 아닌 16이 나옴

## T1-21. 구간 분할 (https://www.kaggle.com/code/agileteam/py-t1-21-expected-question)
# basic1 데이터 중 'age'컬럼 이상치를 제거하고, (이상치는 음수(0포함), 소수점 값)

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
print(df.info())

# age 이상치 (음수(0포함), 소수점 제거)
print('전체 데이터:', df.shape)
df = df[~(df['age'] <= 0)]
print('음수(0포함)값 제거 후 데이터 크기:', df.shape)

df = df[(df['age'] == round(df['age'],0))]
print('소수점 제거 후 데이터 크기:', df.shape)

# 동일한 개수로 나이 순으로 3그룹으로 나눈 뒤 각 그룹의 중앙값을 더하시오
# 기준 확인
pd.qcut(df['age'], q=3) # Categories (3, interval[float64, right]): [(0.999, 38.667] < (38.667, 73.333] < (73.333, 100.0]]

df['range'] = pd.qcut(df['age'], q=3, labels = ['group1', 'group2', 'group3'])
df['range'].value_counts() # 정확히 30개씩 분할
df = df.groupby('range')['age'].median()
print(df.sum())