import streamlit as st
from streamlit_option_menu import option_menu
from page1 import run_page1
from page2 import run_page2 
from page3 import run_page3
#from eda.eda_home import run_eda


def main():
    #total_df = load_data()
    with st.sidebar:
        selected = option_menu(
            "대시보드 메뉴",
            ["데이터 개요", "데이터 분석", "데이터 예측"],
            default_index=0,
        )
    if selected == "데이터 개요":
        run_page1()
    elif selected == "데이터 분석":
        run_page2()
    elif selected == "데이터 예측":
        run_page3()
    else:
        print("error..")


if __name__ == "__main__":
    main()
