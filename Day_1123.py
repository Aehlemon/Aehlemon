# 문제링크: https://www.kaggle.com/code/agileteam/3rd-type2-3-2-baseline

import pandas as pd

train = pd.read_csv("../input/big-data-analytics-certification/t2-1-train.csv")
test = pd.read_csv("../input/big-data-analytics-certification/t2-1-test.csv")
print(train.shape, train.shape)
print(train.head(3))
print(train.info())

# 카테고리 수 확인
train.describe(include="object")
test.describe(include="object")

train['Employment Type'].value_counts()
test['Employment Type'].value_counts()

# 수치형 통계 값
train.describe(exclude="object")
test.describe(exclude="object")
train.isnull().sum()
test.isnull().sum()

train['TravelInsurance'].value_counts()
# 결측치 처리
train['AnnualIncome'] = train['AnnualIncome'].fillna(train['AnnualIncome'].mean())
test['AnnualIncome'] = test['AnnualIncome'].fillna(test['AnnualIncome'].mean())

# target값 변수에 옮기기
target = train.pop('TravelInsurance')
df = pd.concat([train, test])
print(df.shape)

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder

cols = df.select_dtypes(include="object").columns
le = LabelEncoder()

for col in cols:
    df[col] = le.fit_transform(df[col])

# train test 다시 분리
train = df[:train.shape[0]].copy()
test = df[train.shape[0]:].copy()

# 스케일
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
train['AnnualIncome'] = scaler.fit_transform(train[['AnnualIncome']])
test['AnnualIncome'] = scaler.transform(test[['AnnualIncome']])

# # 검증 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(train, target, test_size=0.2, random_state=2022)
X_train.shape, X_val.shape, y_train.shape, y_val.shape

# # 모델 학습 및 평가
# 의사결정나무
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=2022)
model.fit(X_train, y_train)
pred = model.predict_proba(X_val)

# 평가
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_val, pred[:,1]))

# 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=2022)
model.fit(X_train, y_train)
pred = model.predict_proba(X_val)
print(roc_auc_score(y_val, pred[:,1]))

# xgboost
import xgboost as xgb
model = xgb.XGBRFClassifier(random_state=2022)
model.fit(X_train, y_train)
pred = model.predict_proba(X_val)
print(roc_auc_score(y_val, pred[:,1]))

# test 데이터 예측
model = RandomForestClassifier(random_state=2022)
model.fit(X_train, y_train)
pred = model.predict_proba(test)

# 예측한 데이터 -> 데이터프레임으로
submit = pd.DataFrame()
submit['id'] = test['id']
submit['TravelInsurance'] = pred[:,1]

# 예측한 데이터 확인
submit.head()

# csv 저장
submit.to_csv("2022.csv", index=False)
# print(pd.read_csv("2022.csv"))
