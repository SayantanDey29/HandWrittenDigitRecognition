import streamlit as st
import tensorflow as tf
from tensorflow import keras

st.set_page_config(page_title="DigitClassification", page_icon=":shark:", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.set_option('deprecation.showfileUploaderEncoding', False)
hide_st_style="""
    <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
    </style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
@st.cache_resource
def load_model():
    model=tf.keras.models.load_model('Digit.hdf5')
    return model

model=load_model()

st.title("Handwritten Digit Recognition")

file=st.file_uploader("Please upload a image",type=["jpg","png"])
from PIL import Image
import numpy as np

def import_and_predict(img,model):
    img=img.resize((28,28))
    img=np.array(img.convert('L'))
    img=keras.utils.normalize(img,axis=1)
    img=img.reshape(-1,28,28,1)
    prediction=model.predict(img)
    return prediction

if file is None:
    st.markdown("##### There is no image")
else:
    img=Image.open(file)
    st.image(img,use_column_width=True)
    predictions=import_and_predict(img, model)
    num=np.argmax(predictions)
    message=(f'Predicted Value is : {num}')
    val=message.title()
    st.success(val)


