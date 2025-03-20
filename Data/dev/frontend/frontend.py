import streamlit as st
import pandas as pd
import requests
import os

# Получаем URL бэкенда из переменной окружения
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5001")

st.title("Приложение для предсказания")
st.write("Загрузите CSV-файл для получения предсказаний.")

uploaded_file = st.file_uploader("Выберите CSV-файл", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.write("Предварительный просмотр данных:", data.head())
    except Exception as e:
        st.error(f"Ошибка при чтении файла: {e}")

    if st.button("Получить предсказания"):
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
        }
        try:
            response = requests.post(f"{BACKEND_URL}/predict", files=files)
            if response.status_code == 200:
                result = response.json()
                st.success("Предсказания успешно получены!")
                st.write("Результаты предсказания:", result["predictions"])
            else:
                st.error(f"Ошибка: {response.json().get('detail', 'Неизвестная ошибка')}")
        except Exception as e:
            st.error(f"Ошибка при подключении к серверу: {e}")
