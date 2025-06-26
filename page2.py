import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from utils import load_data

df = load_data()

def run_page2(): 
    st.markdown("📈 TITANIC 데이터 분석 대시보드 ")
    page = st.selectbox(" 메뉴를 선택하세요", [
        "1. 🛟 생존자 구조 분석", "2. 🚻 성별 분석", "3. ♾ 나이 분석",
        "4. 🛄 등급 분석", "5. 👨‍👨‍👧‍👦 가족여부 분석"
    ])
    
# 생존자 구조 분석
    if page == "1. 🛟 생존자 구조 분석":
        st.title("👾 생존자 vs 😇 사망자")
        fig = px.pie(df, names='Survived', title='생존자 / 사망자 비율',
                    labels={0: '사망', 1: '생존'})
        st.plotly_chart(fig)
        st.write(df['Survived'].value_counts(normalize=True).rename({0: '사망', 1: '생존'}))
        
        st.markdown("""
                    💡 핵심 인사이트
                    - 사망률이 생존률보다 약 1.6배 높음 확인되었음. 
                    - 구조의 우선순위 또는 생존 조건(예: 성별, 등급, 나이)에 따라 생존률 차이가 클 것으로 예상됨.
                    """)
    
# 성별 분석
    elif page == "2. 🚻 성별 분석":
        st.title("👩‍🦰 성별에 따른 생존률")

        # 성별 생존자 수 vs 전체 수 비교
        st.subheader("성별 생존자 수 vs 전체 수")
        sex_counts = df['Sex'].value_counts()
        sex_survived = df[df['Survived'] == 1]['Sex'].value_counts()
        compare_df = pd.DataFrame({
            '전체 인원': sex_counts,
            '생존자 수': sex_survived
        }).fillna(0)
        compare_df = compare_df.astype(int).reset_index().rename(columns={'index': '성별'})
        fig2 = px.bar(compare_df, x='Sex', y=['전체 인원', '생존자 수'],
                    barmode='group', title='성별 생존자 수와 전체 수 비교')
        st.plotly_chart(fig2)

        st.markdown("""
                    💡 인사이트 :
                    - 여성 승객의 생존률은 약 74.2%로 매우 높았음 ㅣ 남성 승객의 생존률은 약 18.9%에 불과.
                    - 이 따라 여성 승객은 구조 우선 대상이었을 가능성이 높음을 확이됨.
                    """)

# 나이 분석
    elif page == "3. ♾ 나이 분석":
    
        st.subheader("생존/사망자 나이 분포")
        st.plotly_chart(px.histogram(df, x='Age', color='Survived', barmode='overlay'))

        st.subheader("기초 통계")
        st.write(df['Age'].describe())
        
        st.markdown("""
                    📌 요약
                    - 전체 승객의 평균 나이는 약 29.7세
                    - 생존자 그룹의 평균 나이는 약 28세, 사망자 그룹은 30세 이상
                    - 특히 15세 미만의 어린이 생존률이 매우 높음""")
        st.markdown(""" 
                    💡 인사이트
                    - 타이타닉 사고 당시 적용된 “여성과 어린이 우선 구조” 원칙은 나이 분석에서도 뚜렷이 반영됨
                    """)
# 등급 분석
    elif page == "4. 🛄 등급 분석":
        st.title("💼 객실 등급과 생존률")

        # 등급별 생존률
        pclass_group = df.groupby('Pclass')['Survived'].mean().reset_index()
        fig = px.bar(pclass_group, x='Pclass', y='Survived', title='등급별 생존률')
        st.plotly_chart(fig)

        # 등급별 요금 분포 추가
        st.subheader("등급별 요금 분포")
        fig_fare = px.box(df, x='Pclass', y='Fare', title='등급별 요금 Box Plot', points="all")
        st.plotly_chart(fig_fare)

        st.markdown("""
                    📌 요약
                    - 객실 등급은 1등급, 2등급, 3등급으로 구분
                    - 1등급 승객의 생존률이 가장 높고, 3등급 승객은 가장 낮음  
                    """)
        st.markdown(""" 
                     💡 인사이트
                    - 사회적 지위와 재정적 여유가 구조의 우선순위에 큰 영향을 미쳤음을 보여줌
                    - 요금이 높을수록 생존률도 높다는 점은 단순한 위치뿐 아니라 사회적 권한과 정보 접근성의 차이도 영향을 줬음 
                    """)
        
#  가족여부 분석
    elif page == "5. 👨‍👨‍👧‍👦 가족여부 분석":
        st.title(" 가족 여부와 생존률")

        # 가족 여부 정의
        df['Family'] = df['SibSp'] + df['Parch']
        df['Alone'] = df['Family'].apply(lambda x: '혼자' if x == 0 else '동반자 있음')
        fam_group = df.groupby('Alone')['Survived'].mean().reset_index()
        fig = px.bar(fam_group, x='Alone', y='Survived', title='가족 여부에 따른 생존률')
        st.plotly_chart(fig)

        # 연령대 기준 분류
        def age_group(age):
            if age < 15:
                return '어린이'
            elif age > 60:
                return '노인'
            else:
                return '성인'

        df['AgeGroup'] = df['Age'].apply(age_group)

        # 어린이/노인 + 가족 유무 생존률 분석
        st.subheader("연령대(어린이/노인) + 가족 유무 조합 분석")
        elderly_young_df = df[df['AgeGroup'].isin(['어린이', '노인'])]
        group_combo = elderly_young_df.groupby(['AgeGroup', 'Alone'])['Survived'].mean().reset_index()

        fig_combo = px.bar(group_combo, x='AgeGroup', y='Survived', color='Alone', barmode='group',
                        title='어린이/노인 생존률 (가족 동반 여부에 따른 차이)')
        st.plotly_chart(fig_combo)

        st.markdown("""
                    📌 요약
                    -	혼자 탑승한 승객보다 가족(동반자)와 함께한 승객의 생존률이 높음
                    -	특히 어린이 또는 노인 + 가족 동반 조합에서 생존률이 높게 나타남.""")
        st.markdown("""
                    💡 인사이트
                    - 동반 가족이 있을 경우, 서로 구조를 도우며 생존 가능성을 높이는 행동이 나타났을 가능성
                    - 반대로, 혼자 탑승한 승객은 고립되었거나, 구조 우선순위에서 배제될 가능성도 존재
                    """)
        
