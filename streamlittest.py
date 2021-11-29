# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:06:14 2021

@author: rikat
"""

import streamlit as st
import random
kuji1 = ['まったなしだ。','待っていた。。任務完了だ','何の面白みもない。','俺にはもう時間がない。','的を射ている。']

st.title('バーソロミュー・くま')
st.write('わたしはニキュニキュの実の肉球人間 ')

st.write('旅行するならどこへ行きたい？')

text = st.text_input('あなたの名前を教えてください')
'お前の名前は,', text, 'だな。'

s = st.selectbox('好きな気候を選択してほしい',('-','寒帯気候','亜寒帯気候','温帯気候','熱帯気候','乾燥帯気候'))
left_column, right_column = st.columns(2)
button = left_column.button('くま名台詞')
if button:
          
    right_column.write(random.choice(kuji1))
    
if s ==('寒帯気候'):
    st.write('あなたは千葉県千葉市花見川区に飛ばされました')
    st.write('理由：どちらかというと東京に近いので人間性が冷たい人が多そう')
if s ==('亜寒帯気候'):
    st.write ('あなたは千葉県千葉市中央区に飛ばされました')
    st.write('理由：千葉の中心だと思いあがっていて人間性が冷たい人が多そう')
if s ==('温帯気候'):
    st.write ('あなたは千葉県千葉市緑区に飛ばされました')
    st.write('理由：程よい自然で住みやすく人間性が温かい')
if s ==('熱帯気候'):
    st.write ('あなたは千葉県千葉市美浜区に飛ばされました')
    st.write('理由：幕張メッセがあり年中イベントを行っているため熱気がありそう')
if s ==('乾燥帯気候'):
    st.write ('あなたは千葉県千葉市若葉区に飛ばされました')
    st.write('理由：なんか乾燥してそう')
if s==('-'):
    st.write('選択してください')
    

