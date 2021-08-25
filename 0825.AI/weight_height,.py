import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# '남학생'의 몸무게가 주어지면 키를 예측 하고 싶다.


# 1. 데이터준비
pd.set_option("display.width",300)
pd.set_option("display.max_rows",1000)
pd.set_option("display.max_columns",30)

df= pd.read_csv("weight_height.csv")
#print(df)

# 2.1 전처리 - NULL 제거
df = df[['학교명','학년','성별','키','몸무게']]
df.dropna(inplace=True)
#print(df)

# 2.2 전처리 - grade변환 : 123456 123 123 -> 123456 789 10112
#df['학년'] = list(map(lambda x:0 if x[-4]=='초등학교' else (6 if x[-3] =='중학교' else 9),df['학교명']))+df['학년']
def new_column(x):
    if "초등학교" in x:
        return 0
    if "중학교" in x:
        return 3
    if "고등학교" in x:
        return 6
df['grade'] = df['학교명'].apply(new_column) + df['학년']

# 2.3 전처리 - 컬럼정리
df.drop(['학교명','학년'],axis=1,inplace=True)
df.columns=['gender','height','weight','grade']

# 2.4 전처리 - gender 변환 남->0, 여->1
df['gender'] = df['gender'].apply(lambda x: 0 if x=='남' else 1)


# 3. 데이터분할 : 성별에 따라 분리
is_boy= df['gender'] == 0
boy_df, girl_df = df[is_boy],df[~is_boy]

# 데이터분할
x=boy_df['weight']
y=boy_df['height']

# train(학습용) / test(평가용) set분리 : 예측값이 제대로 나오는지 확인하려고 힉습시키지 않은 값으로 테스트
# 30%를 test로 ,반복적으로 돌린다
trainx, testx,trainy,testy = train_test_split(x,y,test_size=0.3,random_state=1)
trainx = trainx.values.reshape(-1,1)
testx = testx.values.reshape(-1,1)

# 모델준비
linear = LinearRegression()

# 학습
linear.fit(trainx,trainy)

# 예측 및 평가
predict = linear.predict(testx)
print(testx)
print(predict)
print(testy)

# 그래프
plt.plot(testx,testy,"b.")
plt.plot(testx,predict,"r.")

plt.xlim(10,140)
plt.ylim(100,220)
plt.grid()
plt.show()

# 몸무게 80일때 키는?
pred_grd = linear.predict([[80]])
print("남학생키 예측 ",pred_grd)
