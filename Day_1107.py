df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df.head()
df.info()

# 이상치 (소수점 나이) 찾기 (https://www.kaggle.com/code/agileteam/py-t1-2-expected-questions)

sub = df[df['age'] != 0]
print(len(sub)) 

# 올림, 내림, 버림의 평균값 구하고 전체 총합 구하기

m_ceil = np.ceil(sub['age']).mean()
m_floor = np.floor(sub['age']).mean()
m_trunc = np.trunc(sub['age']).mean()

result = m_ceil + m_floor + m_trunc
round(result,0) 


# <결측치 처리 https://www.kaggle.com/code/agileteam/py-t1-3-map-expected-questions>
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
#df.head()
df.isnull().sum()

# 결측치 비율 확인
f1_d = df['f1'].isnull().sum() / len(df)
f3_d = df['f3'].isnull().sum() / len(df)

print(f1_d > 0.8)
print(f3_d > 0.8)

# df.drop('f3', axis=1, inplace=True)
df.shape # 삭제 완료

# city 별 중앙값으로 대체

df['city'].unique()
s_m = df[df['city'] == '서울']['f1'].median()
b_m = df[df['city'] == '부산']['f1'].median()
d_m = df[df['city'] == '대구']['f1'].median()
k_m = df[df['city'] == '경기']['f1'].median()

s_m, b_m, d_m, k_m

# groupby를 통해서도 확인 가능

s, b, d, k = df.groupby('city')['f1'].median()
s, b, d, k

# 대체전 샘플 출력
sub = df[df['f1'].isna() == True]
# print(sub.head(4))

# f1결측치 city별 중앙값으로 대체

df['f1'] = df['f1'].fillna(df['city'].map({'서울': s_m, '부산': b_m, '대구': d_m, '경기': k_m}))

# 대체 후 결측치 확인
print(df['f1'].isnull().sum())

# f1 컬럼의 평균값
df['f1'].mean()