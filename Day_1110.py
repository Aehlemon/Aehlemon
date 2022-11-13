## T1-8. 누적합 그리고 보간(결측치 처리) - https://www.kaggle.com/code/agileteam/py-t1-8-expected-questions
import numpy as np
import pandas as pd

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
#print(df.head(3))
#print(df.info())

# 1) 주어진 데이터 셋에서 'f2' 컬럼이 1인 조건에 해당하는 데이터의 'f1'컬럼 누적합을 계산

df2 = df[df['f2'] == 1]['f1'].cumsum()
print(df2[:20])

# 2) 누적합 결측치는 바로 뒤의 값을 채우고, 누적합의 평균값을 출력한다. (단, 결측치 바로 뒤의 값이 없으면 다음에 나오는 값을 채워넣는다)

df2 = df2.fillna(method='bfill')
# print(df2[:20])
result = df2.mean()
print(result)

## T1-9. 수치형 변수 표준화 (https://www.kaggle.com/code/agileteam/py-t1-9-expected-questions)
# 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 그 중앙값을 구하시오.: StandardScaler 활용

# 표준화 모듈 import 예시 확인
from sklearn.preprocessing import StandardScaler

# data =[[0,2], [0.4, 0.2], [1.5, 0.3], [32, 29], [14, 11], [5, 40]]
# scaler = StandardScaler()
# print(scaler.fit(data))
# print(scaler.transform(data))

scaler = StandardScaler()
df['f5'] = scaler.fit_transform(df[['f5']])
print(df['f5'].median())


## T1-10.여-존슨과 박스-칵스 변환 (method = 'box-cox')
# https://www.kaggle.com/code/agileteam/py-t1-10-expected-questions

# 'yeo-johnson' 변환 : 실수 전체에 대해 일반화 (데이터가 양수, 음수 모두 됨)
# 'box-cox' 변환: 데이터를 정규분포에 가깝게 만들어 데이터 분산을 안정화하는 것
# - (데이터가 양수일 때) 정규성을 가정하는 분석법이나 정상성이 요구되는 분석법을 사용하기에 앞서 전처리 과정에서 사용하는 것
# - 보통은 데이터의 최솟값이 양수가 되도록 어떤 값을 더해서 밀어주는 식(shift)로 해결

# import numpy as np
from sklearn.preprocessing import power_transform
# data = [[1, 3], [4, 3], [2, 7]]
# print(power_transform(data, method='box-cox')) # default: yeo-johnson

# 1) 주어진 데이터에서 20세 이상인 데이터를 추출하고 'f1'컬럼을 결측치를 최빈값으로 채운 후
df = df[df['age'] >= 20]
print(df.head(5))
print(df['f1'].isnull().sum())
# print(df['f1'].mode())
f1_mode = df['f1'].mode()
df['f1'] = df['f1'].fillna(f1_mode[0])
print(df['f1'].isnull().sum())

# 2) f1 컬럼의 여-존슨과 박스콕스 변환 값을 구하고
# standardize=False 는 선택 사항

df['y'] = power_transform(df[['f1']])
print(df['y'].head())
df['b'] = power_transform(df[['f1']], method='box-cox')
print(df['b'].head())

# 3) 두 값의 차이를 절대값으로 구한다음 모두 더해 소수점 둘째 자리까지 출력(반올림)하시오
print(round(sum(np.abs(df['y'] - df['b'])),2))

