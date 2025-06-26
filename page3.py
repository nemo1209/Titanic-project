import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from utils import load_data


# @st.cache_data
# def load_data():
#     df = pd.read_csv("/Users/dongvantruong/PROJECT/titanic_project/data_file/train.csv")
#     return df

# Preprocessing
df = load_data()
processed_df = df.copy()
processed_df['Sex'] = processed_df['Sex'].map({'male': 0, 'female': 1})
processed_df['Embarked'] = processed_df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
imp = SimpleImputer(strategy='mean')
processed_df['Age'] = imp.fit_transform(processed_df[['Age']])
processed_df['Embarked'] = processed_df['Embarked'].fillna(0)

def run_page3():
    st.title("🔮 생존 확률 예측기")
    st.write("""
            - train 파일을 분석한 데이터 모듈 바탕으로 생촌 확률 예측 모텔 입니다.
            - 아래 정보를 입력하면 생존 확률을 예측 가능합니다.
             """)

    pclass = st.selectbox("객실 등급 (1=1등급, 3=3등급)", [1, 2, 3])
    sex = st.selectbox("성별", ['남성', '여성'])
    age = st.slider("나이", 0, 80, 30)
    sibsp = st.number_input("형제/배우자 수", 0, 8, 0)
    parch = st.number_input("부모/자녀 수", 0, 6, 0)
    fare = st.slider("탑승 요금", 0.0, 600.0, 32.0)
    #embarked = st.selectbox("탑승 항구", ['S', 'C', 'Q'])

    sex_val = 0 if sex == '남성' else 1
    embarked_val = {'S': 0, 'C': 1, 'Q': 2}

    input_data = pd.DataFrame([[pclass, sex_val, age, sibsp, parch, fare]],
                               columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'])

    model = RandomForestClassifier()
    model.fit(processed_df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']], processed_df['Survived'])

    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)

    st.subheader("예측 결과 확인")
    if prediction[0] == 1:
        st.success(f"🌟 이 승객은 생존할 확률이 높습니다! (생존 확률: {proba[0][1]*100:.2f}%)")
    else:
        st.error(f"☠️ 이 승객은 사망할 가능성이 높습니다. (생존 확률: {proba[0][1]*100:.2f}%)")