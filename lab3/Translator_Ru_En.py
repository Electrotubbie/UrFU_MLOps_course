#Устанавливаем библиотеку
#pip install transformers sentencepiece

from transformers import pipeline

#Сосзаем пайплан для модели перевода с русского на анлийский язык
classifier = pipeline(model="Helsinki-NLP/opus-mt-ru-en")

#Вводим текст на русском языке для обработки моделью!
text_eng = classifier(input())

#Выводим результат перевода на английском языке!
print(text_eng)
