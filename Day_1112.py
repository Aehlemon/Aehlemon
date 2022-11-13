# 문제 링크: https://www.kaggle.com/code/agileteam/4th-type1-python
## 작업형1 문제
### 1-1. age 컬럼의 3사분위수와 1사분위수의 차를 절대값으로 구하고, 소수점 버려서, 정수로 출력

import pandas as pd
import numpy as np

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

print(df.head())
print(df.info())

Q3 = df['age'].quantile(0.75)
Q1 = df['age'].quantile(0.25)
print(int(np.trunc(abs(Q3-Q1))))

### 1-2.(loves반응+wows반응)/(reactions반응) 비율이 0.4보다 크고 0.5보다 작으면서, status_type 컬럼이 'video'인 데이터의 갯수
import pandas as pd
import numpy as np

df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/fb.csv")
print(df.head(4))
print(df.info())
df['Index'] = df['loves']+df['wows']/df['reactions']
print(df.head(4))

cond1 = df['Index'] > 0.4
cond2 = df['Index'] < 0.5
cond3 = df['type'] == 'video'
 
print(len(cond1 & cond2 & cond3))

### 1-3. date_added가 2018년 1월 이면서 country가 United Kingdom 단독 제작인 데이터의 갯수

import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")
print(df.head(4))
print(df.info())

# 날짜 2018년 1월인 것만 추출하기 위해 datetime 컬럼 생성 
df['date_add'] = pd.to_datetime(df['date_added'])

# (방법1) 개별 조건으로 join
df['year'] = df['date_add'].dt.year
df['month'] = df['date_add'].dt.month
print(df.head(5))

cond1 = df['year'] == '2018'
cond2 = df['month'] == '1'
cond3 = df['country'] == 'United Kingdom'
print(len(df[cond1 & cond2 & cond3]))

# (방법2) 'yyyy-mm-dd' 이용
# df['date_added'] = pd.to_datetime(df['date_added'])
cond1 = df['date_added'] >= '2018-1-1'
cond2 = df['date_added'] <= '2018-1-31'
cond3 = df['country'] == 'United Kingdom'
print(len(df[cond1 & cond2 & cond3]))

# (방법3) Between 이용; 제일 간편한 듯
df['date_added'] = pd.to_datetime(df['date_added'])
cond1 = df['date_added'].between('2018-1-1', '2018-1-31')
cond2 = df['country'] == 'United Kingdom'
print(len(df[cond1& cond2]))

# (추가) 문자열 대소문 섞여있고, 공백 있으면
# 띄어쓰기 제거
df['country'] = df['country'].str.replace(' ','')

# 소문자로 변경
df['country'] = df['country'].str.lower()
df['country']
