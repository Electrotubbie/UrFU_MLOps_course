from fastapi.testclient import TestClient
from Translator_ru_en_FastAPI import app

client = TestClient(app)

def test_read_FAstApi_Translator():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Приветствую Тебя в API обученной модели по переводу русского языка на английский!"

def test_predict_post_1_FAstApi_Translator():
    response = client.post("/predict/",
                         json={"text": "Привет, Василий!"})
    json_data = response.json()
    assert response.status_code == 200
    assert response.json() == "Перевод на английский язык: Hey, Vasily!"

def test_predict_post_2_FAstApi_Translator():
    response = client.post("/predict/",
                         json={"text": "На улице прекрасная погода, пошли гулять!"})
    json_data = response.json()
    assert response.status_code == 200
    assert response.json() == "Перевод на английский язык: Beautiful weather outside, let's go for a walk!"
