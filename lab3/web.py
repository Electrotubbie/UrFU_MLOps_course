from transformers import pipeline
import streamlit as st

classifier = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")
st.title('Определитель языка')
text = st.text_input('Введите текст:')
result = st.button('Нажми, что бы определить!')
if result:
    text_eng = classifier(text)
    st.subheader('Язык, на котором написан текст:')
    st.markdown(text_eng)
else:
    st.write('Ожидание текста для определения языка')
