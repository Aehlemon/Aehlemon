# https://www.kaggle.com/code/agileteam/t2-1-titanic-simple-baseline
# 시험환경 세팅
from sklearn.model_selection import train_test_split
def exam_data_load(df, target, id_name="", null_name=""):
    if id_name == "":
        df = df.reset_index().rename(columns={"index": "id"})
        id_name = 'id'
    else:
        id_name = id_name
    
    if null_name != "":
        df[df == null_name] = np.nan
        
    X_train, X_test = train_test_split(df, test_size=0.2, random_state=123)
    y_train = X_train[[id_name, target]]
    X_train = X_train.drop(columns=[target])

    y_test = X_test[[id_name, target]]
    X_test = X_test.drop(columns=[target])

    return X_train, X_test, y_train, y_test


df = pd.read_csv("../input/c/titanic/train.csv")
print(df.head(5))
print(df.info())

# 학습, 평가데이터 분리
X_train, X_test, y_train, y_test = exam_data_load(df, target='Survived', id_name='PassengerId')
X_train.shape, X_test.shape, y_train.shape, y_test.shape

print(X_train.head(4))
print(X_train.info())
print(y_train.head(4))
print(y_train['Survived'].value_counts())

# 더미변수 처리
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(X_train[features])
test = pd.get_dummies(X_test[features])
# print(X)
# print(test)
print(X.shape, test.shape) # 성별 대로 더미변수 되어서 컬럼+1개
y = y_train['Survived']

# 모델 생성 및 평가
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=200, max_depth = 7, random_state=2021)
model.fit(X, y)
predictions = model.predict(test)
# print(predictions[:5])
score = model.score(X,y)
print(score)

# 제출형식 맞추기
output = pd.DataFrame({'PassengerId': X_test.PassengerId, 'Survived': predictions})
print(output.head(5))
output.to_csv('20221119.csv', index=False, encoding='utf-8-sig')