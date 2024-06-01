from transformers import pipeline
import streamlit as st

classifier = pipeline(model="Helsinki-NLP/opus-mt-ru-en")
st.title('Перевод текста на английский язык')
text = st.text_input('Введите текст на русском языке')
result = st.button('Нажми, что бы перевести!')
if result:
    text_eng = classifier(text)
    st.subheader('Перевод:')
    st.markdown(text_eng[0]['translation_text'])
else:
    st.write('Ожидание текста для перевода')
