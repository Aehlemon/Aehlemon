## T1-16. 분산 (https://www.kaggle.com/code/agileteam/py-t1-16-expected-question)
import numpy as np
import pandas as pd

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
print(df.head(4))

# 주어진 데이터 셋에서 f2가 0값인 데이터를 age를 기준으로 오름차순 정렬하고
df = df[df['f2'] == 0].sort_values('age')

# 앞에서 부터 20개의 데이터를 추출한 후 
df = df[:20]

# f1 결측치(최소값)를 채우기 전과 후의 f1분산 차이를 계산하시오 (소수점 둘째 자리까지)
prior_var = df['f1'].var()
print(prior_var)

df['f1'] = df['f1'].fillna(df['f1'].min())
post_var = df['f1'].var()
print(post_var)

answer = prior_var - post_var
print(round(answer, 2))

## T1-17. 시계열 데이터1 (https://www.kaggle.com/code/agileteam/py-t1-17-1-expected-question)
# 2022년 5월 sales의 중앙값을 구하시오

df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
# print(df.head(4))
# print(df.info())
# print(df.describe())

# 날짜로 변환
df['year'] = pd.to_datetime(df['Date']).dt.year
df['month'] = pd.to_datetime(df['Date']).dt.month
# print(df.head(5))
print(df.describe()) # 2022~2023
may_2022 = (df['year'] == 2022) & (df['month'] == 5)
print(df[may_2022]['Sales'].median())


## T1-18. 시계열 데이터2 (https://www.kaggle.com/code/agileteam/py-t1-18-2-expected-question)
# 2022년 5월 주말과 평일의 sales컬럼 평균값 차이를 구하시오 (소수점 둘째자리까지 출력, 반올림)
# 위 데이터 활용

# Day 와 dayofweek 만들기
df['day'] = pd.to_datetime(df['Date']).dt.day
df['dayofweek'] = pd.to_datetime(df['Date']).dt.dayofweek # 0~6
print(df.head(5))

# 주말과 평일 구분
df['weekend'] = df['dayofweek'].apply(lambda x: x>=5, 1, 0)
print(df.head(4))

weekend_cond = (df['year']==2022) & (df['month']==5) & (df['weekend'])
weekday_cond = (df['year']==2022) & (df['month']==5) & (~df['weekend'])
weekend = df[weekend_cond]['Sales'].mean()
weekday = df[weekday_cond]['Sales'].mean()
print(round(weekend - weekday, 2))