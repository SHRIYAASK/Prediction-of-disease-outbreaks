import streamlit as st
from PIL import Image


st.set_page_config(page_title='Prediction of Heart Disease',
                   layout='wide',
                   page_icon="🧑‍⚕️")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f6eee0 ;
        color:#523a28;

    }
    
    </style>
    """,
    unsafe_allow_html=True
)
# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "main"
   

# Page Navigation Logic
if st.session_state["page"] == "diabetes":
    st.switch_page("pages/diabetes.py")
elif st.session_state["page"]=="heart":
    st.switch_page("pages/heart.py")
elif st.session_state["page"]=="parkinsons":
    st.switch_page("pages/parkinsons.py")

# Layout
st.title("Medical Disease Prediction")

# Create 3 containers in the same row
col1, col2, col3 = st.columns(3)


image1 = Image.open("images/download.png")
diabetes_img = image1.resize((300, 200))  # Width: 300px, Height: 200px
image2 = Image.open("images/heart.png")
heart_img = image2.resize((300, 200))  # Width: 300px, Height: 200px
image3 = Image.open("images/parkinsons.png")
parkinsons_img = image3.resize((300, 200))  # Width: 300px, Height: 200px



with col1:
    with st.container():
        st.image(diabetes_img,use_container_width=True)
        st.subheader("Diabetes Disease")
        if st.button("Check Diabetes"):
            st.session_state["page"] = "diabetes"
            st.rerun()

with col2:
    with st.container():
        st.image(heart_img, use_container_width=True)
        st.subheader("Heart’s Disease")
        if st.button("Check heartdisease"):
            st.session_state["page"] = "heart"
            st.rerun()

with col3:
    with st.container():
        st.image(parkinsons_img, use_container_width=True)
        st.subheader("Parkinson's Prediction")
        if st.button("Check Parkinsons"):
            st.session_state["page"] = "parkinsons"
            st.rerun()
