## T1-14. 2개 조건에 따른 상위 값 (https://www.kaggle.com/code/agileteam/py-t1-14-2-expected-question)
import pandas as pd
import numpy as np

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
print(df.head(4))
# print(df.info())

# 1) city와 f4 (MBTI)를 기준으로 f5의 평균값을 구하기
df = df.groupby(['city', 'f4'])[['f5']].mean()
print(df)


# f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)
df = df.sort_values('f5', ascending=False).head(7)
print(df)
print(round(df['f5'].sum(), 2))

## T1-15. 슬라이싱 & 조건 (https://www.kaggle.com/code/agileteam/py-t1-15-expected-question)
# 주어진 데이터 셋에서 age컬럼 상위 20개의 데이터를 구한 다음
import pandas as pd
import numpy as np

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
print(df.head(4))

df = df.sort_values('age', ascending=False).head(20)
print(df)

# f1의 결측치를 중앙값으로 채운다.
f1_m = df['f1'].median()
# print(f1_m)
df['f1'] = df['f1'].fillna(f1_m)
# print(df)

# f4가 ISFJ와 f5가 20 이상인 f1의 평균값을 출력하시오!
cond = (df['f4'] == 'ISFJ') & (df['f5'] >= 20)
result = df[cond]['f1'].mean()
print(result)