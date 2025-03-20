import os
import io
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="Simple Prediction API", version="1.0")

# Глобальная переменная для хранения модели
model = None

# При запуске приложения загружаем модель из файла best_xgb_model.pkl
@app.on_event("startup")
def load_model():
    global model
    model_path = "best_xgb_model.pkl"
    if not os.path.exists(model_path):
        raise RuntimeError(f"Модель {model_path} не найдена!")
    model = joblib.load(model_path)

# Эндпоинт для предсказания: принимает CSV-файл и возвращает предсказания
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка чтения файла: {e}")
    
    try:
        predictions = model.predict(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при выполнении предсказания: {e}")
    
    return JSONResponse(content={"predictions": predictions.tolist()})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="0.0.0.0", port=5001)
