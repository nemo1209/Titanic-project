
import streamlit as st

def run_page1():
    st.title("🚢 타이타닉 생존자 분석 프로젝트")
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg", use_column_width=True)
    st.markdown("""
    ### 📊 프로젝트 개요
    - 타이타닉 호의 승객 데이터를 바탕으로 생존률을 분석합니다.
    - 데이터 분석 바탕으로 생존-사망 확률 예측 모텔을 도출합니다. 
  
    ### 📁 데이터셋 구성
    
    - **Survived**: 생존 여부 (0 = 사망, 1 = 생존)
    - **Pclass**: 티켓 등급 (1, 2, 3)
    - **Sex**: 성별
    - **Age**: 나이
    - **SibSp**, **Parch**: 동반한 가족 수
    - **Fare**: 탑승 요금
    
    """)