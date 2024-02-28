import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app predicts the **Advertising Sales** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.7, 297, 100)
    Radio = st.sidebar.slider('Radio', 0, 50, 15)
    Newspaper = st.sidebar.slider('Newspaper', 0.3, 114, 20)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features
