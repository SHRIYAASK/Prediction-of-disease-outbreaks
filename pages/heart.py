import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu
import numpy as np

st.set_page_config(page_title='Prediction of Heart Disease',
                   layout='wide',
                   page_icon="🧑‍⚕️")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f6eee0 ;
        color:#523a28;

    .stTextInput > div > div > input {
        background-color:#d0b49f ;
        color:#a47551;
        border: #d0b49f;
        padding: 10px ;
        border-radius: 5px ;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)
heart_model= pickle.load(open(r"D:/prediction/training_datset/heart_model.sav",'rb'))

st.title('Heart Disease Prediction')
col1,col2,col3 = st.columns(3)
with col1:
    Age= st.text_input('Age')
with col2:
    Sex= st.text_input('Sex')
with col3:
    cp= st.text_input('cp')
with col1:
    Trestbps = st.text_input('Trestbps')
with col2:
    Cholestral= st.text_input('Cholestral')
with col3:
    fbs= st.text_input('fbs')
with col1:
    restecg= st.text_input('restecg')
with col2:
    Thalach= st.text_input('Thalach')
with col3:
    Exang=st.text_input("Exang")
with col1:
    Oldpeak=st.text_input("Oldpeak")
with col2:
    Slope=st.text_input("Slope")
with col3:
    Ca=st.text_input("Ca")
with col1:
    Thal=st.text_input("Thal")

heart_diagnosis = ''
if st.button('heart Disease Test Result'):
    user_input=[Age,Sex,cp,Trestbps,Cholestral,fbs,restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal]
    user_input= [float(x) for x in user_input]
    heart_prediction= heart_model.predict([user_input])
    if heart_prediction[0]==1:
        heart_diagnosis= 'The person has a defective heart'
    else:
        heart_diagnosis= 'The person has normal heart'
st.success(heart_diagnosis)


if st.button("Go Back"):
    st.session_state["page"] = "main"
    st.switch_page("D:\Aicte internship\dashboard.py")
    st.rerun()