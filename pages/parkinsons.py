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
parkinsons_model= pickle.load(open(r"D:/prediction/training_datset/parkinsons.sav",'rb'))

st.title('parkinsons Disease Prediction')
col1,col2,col3 = st.columns(3)
with col1:
    Fo_Hz= st.text_input('MDVP:Fo(Hz)')
with col2:
    Fhi_Hz= st.text_input('MDVP:Fhi(Hz)')
with col3:
    Flo_Hz= st.text_input('MDVP:Flo(Hz)')
with col1:
    Jitter = st.text_input('Jitter%')
with col2:
    Jitterabs= st.text_input('Jitter(abs)')
with col3:
    RAP = st.text_input('MDVP:RAP')
with col1:
    PPQ = st.text_input('MDVP:PPQ')
with col2:
    DDP= st.text_input('Jitter:DDP')
with col3:
    Shimmer=st.text_input("MDVP:Shimmer")
with col1:
    db=st.text_input("MDVP:Shimmer(db)")
with col2:
    APQ3=st.text_input("Shimmer:APQ3")
with col3:
    APQ5=st.text_input("Shimmer:APQ5")
with col1:
    APQ=st.text_input("MDVP:APQ")
with col2:
    DDA= st.text_input('Shimmer: DDA')
with col3:
    NHR=st.text_input("NHR")
with col1:
    HNR=st.text_input("HNR")
with col2:
    RPDE= st.text_input('RPDE')
with col3:
    DFA=st.text_input("DFA")
with col1:
   spread1=st.text_input("Spread1")
with col2:
    spread2= st.text_input('Spread2')
with col3:
    D2=st.text_input("D2")
with col1:
    PPE=st.text_input("PPE")



parkinsons_diagnosis = ''
if st.button("Parkinson's Disease Test Result"):
    user_input=[Fo_Hz,Fhi_Hz,Flo_Hz,Jitter,Jitterabs,RAP,PPQ,DDP,Shimmer,db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
    user_input= [float(x) for x in user_input]
    parkinsons_prediction= parkinsons_model.predict([user_input])
    if parkinsons_prediction[0]==1:
        parkinsons_diagnosis= 'The person has parkinsons disease'
    else:
        parkinsons_diagnosis= 'The person is normal'
st.success(parkinsons_diagnosis)


if st.button("Go Back"):
    st.session_state["page"] = "main"
    st.switch_page("D:\Aicte internship\dashboard.py")
    st.rerun()