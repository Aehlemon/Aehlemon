## T1-11. min-max 기준 상하위 5%값 (https://www.kaggle.com/code/agileteam/py-t1-11-min-max-5-expected-questions)
import pandas as pd
import numpy as np

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
print(df.head(4))
print(df.info())
print(df.isnull().sum())

# 방법1
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['f5_1'] = scaler.fit_transform(df[['f5']])

print(df.info())
print(df.isnull().sum())

# 방법2
df['f5_2'] = df['f5'].transform(lambda x: ((x - x.min()) / (x.max() - x.min())))
print(df.head(5))

# 방법 1과 2 차이: 튀는 값이 있긴 있음
df['check'] = df['f5_1'] - df['f5_2']
print(df.head(10))

# 상위 5%와 하위 5%의 합

result = df['f5_1'].quantile(0.95) + df['f5_1'].quantile(0.05)
print(result)

## T1-12. 상위 10개, 하위 10개 차이 (https://www.kaggle.com/code/agileteam/py-t1-12-10-10-expected-questions)
df = pd.read_csv("../input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv")
print(df.head(4))
print(df.info())

df.drop('Unnamed: 0', axis=1, inplace=True)
df2 = df.groupby("country").max() # 국가별 상황 확인
print(df2)

df2 = df2.sort_values('ratio', ascending=False)
print(df2.ratio) # Gibraltar, Malta 100% 넘음
# print(df2.ratio <= 100)

sub= df2.ratio[3:] # 이상치 제거 후
answer = sub.head().mean() - sub.tail().mean()
print(round(answer,1))

## T1-13. 상관관계 구하기 (https://www.kaggle.com/code/agileteam/py-t1-13-expected-questions)
import pandas as pd
import numpy as np

df = pd.read_csv("../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv")
# print(df.head())
print(df.corr())

corr = df.corr()[:-1] # 자기 상관관계 제거 1
print(corr['quality'])
print(abs(corr['quality']).max() + abs(corr['quality']).min())
answer3 = abs(corr['quality']).max() + abs(corr['quality']).min()
print(round(answer3, 2))