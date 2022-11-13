## T1-5. 조건에 맞는 데이터 표준편차 구하기 (https://www.kaggle.com/code/agileteam/py-t1-5-expected-questions)
# - 주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오
import numpy as np
import pandas as pd

data = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
enfj = data[data['f4'] == 'ENFJ']
infp = data[data['f4'] == 'INFP']
result = np.abs(enfj['f1'].std() - infp['f1'].std())
print(result)


## T1-6. 결측치 제거 및 그룹 합계 (https://www.kaggle.com/code/agileteam/py-t1-6-expected-questions)
# 주어진 데이터 중 basic1.csv에서 'f1'컬럼 결측 데이터를 제거하고, 
# 'city'와 'f2'을 기준으로 묶어 합계를 구하고, 'city가 경기이면서 f2가 0'인 조건에 만족하는 f1 값을 구하시오

import numpy as np
import pandas as pd

data = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
print(data['f1'].isnull().sum()) #31
data = data[~data['f1'].isnull()] # dropna()는 결측치가 1개라도 있으면 또는 전체이면 행 또는 컬럼이 삭제되어 pass
print(data['f1'].isnull().sum()) #0
# print(data.groupby(['city','f2']).sum())
sub = data.groupby(['city','f2']).sum()
print(sub.iloc[0]['f1']) # 833

## T1-7. 값 변경 및 2개 이상의 조건 (https://www.kaggle.com/code/agileteam/py-t1-7-2-expected-questions)
# 'f4'컬럼의 값이 'ESFJ'인 데이터를 'ISFJ'로 대체하고, 

import numpy as np
import pandas as pd

data = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
print(data.head(4))
esfj = data[data['f4'] == 'ESFJ']
# print(esfj.head(4))
data['f4'].replace('ESFJ', 'ISFJ', inplace=True)
esfj = data[data['f4'] == 'ESFJ']
# print(esfj.head(4))

# 'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력하시오
result = data[(data['f4'] == 'ISFJ') & (data['city'] == '경기')]['age'].max()
print(result)
