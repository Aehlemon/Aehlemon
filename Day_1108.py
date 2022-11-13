# 문제 링크: https://www.kaggle.com/code/agileteam/py-t1-4-expected-questions

import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_csv("../input/house-prices-advanced-regression-techniques/train.csv")
df['SalePrice'].head()

#df.head(5)

# EDA (시험에서는 시각화 불가)
df['SalePrice'].hist()

# 'SalePrice'컬럼 왜도와 첨도계산
s1 = df['SalePrice'].skew()
k1 = df['SalePrice'].kurt()
print("왜도:" ,s1)
print("첨도:" ,k1)

# 'SalePrice'컬럼 로그변환
df['SalePrice'] = np.log1p(df['SalePrice'])

# EDA (시험에서는 시각화 불가): 히스토그램으로 변환된 모습 확인
df['SalePrice'].hist()

# 'SalePrice'컬럼 왜도와 첨도 다시 계산
s2 = df['SalePrice'].skew()
k2 = df['SalePrice'].kurt()
print("왜도:" ,s2)
print("첨도:" ,k2)

# 모두 더하고 출력
print(round(s1+s2+k1+k2,2)) 