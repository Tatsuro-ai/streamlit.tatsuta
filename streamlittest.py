# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:06:14 2021

@author: rikat
"""

import streamlit as st

st.write('こんにちは')

text = st.text_input('あなたの名前を教えてください')
'あなたの名前は,', text, 'です'


from PIL import image
img = Image.open('IMG_E4380.JPG')
st.image(img, caption='写真の説明',use_column_width=True)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
right_column.write('ここは右カラムです')
