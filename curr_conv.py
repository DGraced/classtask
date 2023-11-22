import streamlit as st
from PIL import Image

st.title("Currency Convertor")
st.text(' Graced currency converter will show you how much your money is worth in other')
st.text(' currencies at the real exchange rate. You can convert over 5 currencies quickly')
img = Image.open("cu.jpg")
st.image(img.resize((250,250)))

curr =['Naira', 'Pounds', 'Dollar', 'Euros', 'Yen', 'Cedis']
conv =[1, 1023, 816, 114, 68]

def convert(num,initial,final):
    int_id = curr.index(initial)
    fin_id = curr.index(final)

    value1 = conv[int_id]
    value2 = conv[fin_id]

    result = num * value1 / value2

    return result

col1, col2, col3 = st.columns(3)

with col1:
    num = st.number_input('How much are you converting?')

with col2:
    initial = st.selectbox ('Amount Currency', curr)

with col3:
    final = st.selectbox('Conversion Currency', curr)


amount = convert(num, initial, final)

if st.button('Convert'):
    st.write(amount)