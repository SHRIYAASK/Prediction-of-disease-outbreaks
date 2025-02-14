import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
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
diabetes_model= pickle.load(open(r"D:/prediction/training_datset/diabetes_model.sav",'rb'))

st.title('Diabetes Prediction using Ml')
col1,col2,col3 = st.columns(3)
with col1:
    Pregnancies= st.text_input('Number of Pregnancies')
with col2:
    Glucose= st.text_input('Glucose level')
with col3:
    Bloodpressure= st.text_input('Blood Pressure value')
with col1:
    SkinThickness = st.text_input('Skin Thickness value')
with col2:
    Insulin= st.text_input('Insulin level')
with col3:
    BMI = st.text_input('BMI  value')
with col1:
    DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
with col2:
    Age= st.text_input('Age of the person')

diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
    user_input= [float(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis= 'The person is diabetic'
    else:
        diab_diagnosis= 'The person is not diabetic'
st.success(diab_diagnosis)


if st.button("Go Back"):
    st.session_state["page"] = "main"
    st.switch_page("D:\Aicte internship\dashboard.py")
    st.rerun()