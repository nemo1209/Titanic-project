import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("/Users/dongvantruong/PROJECT/titanic_project/data_file/train.csv")
    return df

df = load_data()