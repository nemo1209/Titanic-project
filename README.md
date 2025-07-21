# 🚢 Titanic Dataset 분석 웹 애플리케이션 (Streamlit)

이 프로젝트는 **Titanic 탑승객 데이터**를 활용하여 Streamlit으로 만든 **멀티 페이지 웹 앱**입니다.  
탑승객 정보 시각화, 필터링, 통계 요약 등을 제공합니다.

## 🔍 주요 기능

- Streamlit 기반 웹 UI
- 다중 페이지 구성 (page1 ~ page3)
- CSV 파일을 통한 데이터 분석
- 탑승객 필터링 및 간단한 통계 출력
- 시각화 및 사용자 입력 UI 포함

## 📁 데이터 설명

사용된 데이터: `test.csv`  
출처: [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data)

| 컬럼명       | 설명                             |
|--------------|----------------------------------|
| PassengerId  | 승객 ID                          |
| Pclass       | 좌석 등급 (1~3등석)              |
| Name         | 이름                             |
| Sex          | 성별                             |
| Age          | 나이                             |
| SibSp        | 형제/배우자 수                   |
| Parch        | 부모/자녀 수                     |
| Ticket       | 티켓 번호                        |
| Fare         | 요금                             |
| Cabin        | 선실 정보                        |
| Embarked     | 탑승 항구 (C, Q, S)              |

## 📂 프로젝트 구조
project/
├── main_app.py      # 앱 실행 파일
├── page1.py         # 입력 UI 페이지
├── page2.py         # 데이터 시각화 페이지
├── page3.py         # 분석 및 통계 요약
├── test.csv         # Titanic 탑승객 데이터
└── README.md
