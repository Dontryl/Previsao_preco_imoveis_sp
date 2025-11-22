from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Any
import pickle
import os
import pandas as pd

from preprocessing import create_features, load_data
from train import prepare_data, train_model, evaluate_model

MODEL_PATH = "modelo.pkl"

app = FastAPI(title="API - Previsão Preço Imóveis SP")


class TrainResponse(BaseModel):
    r2: float
    mae: float
    model_path: str


class PredictItem(BaseModel):
    # aceita qualquer dicionário de pares coluna:valor
    data: dict


def load_model(path: str = MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError("Modelo não encontrado. Treine e salve o modelo primeiro (/train).")
    with open(path, "rb") as f:
        payload = pickle.load(f)
    return payload["model"], payload["feature_columns"]


@app.post("/train", response_model=TrainResponse)
def train_and_save(caminho: Optional[str] = None, save_path: str = MODEL_PATH):
    # Treina o modelo usando pipeline e salva o modelo + colunas
    df = load_data(caminho)
    df_encoded = create_features(df)
    X_train, X_test, y_train, y_test = prepare_data(df_encoded, target_col="Price")
    model = train_model(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)

    payload = {"model": model, "feature_columns": X_train.columns.tolist()}
    with open(save_path, "wb") as f:
        pickle.dump(payload, f)

    return TrainResponse(r2=metrics["r2"], mae=metrics["mae"], model_path=save_path)


@app.post("/predict")
def predict(item: PredictItem):
    try:
        model, feature_columns = load_model()
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    # Constrói DataFrame a partir do input, aplica create_features e alinha colunas
    df_in = pd.DataFrame([item.data])
    df_enc = create_features(df_in)

    # Remover coluna alvo caso enviada
    if "Price" in df_enc.columns:
        df_enc = df_enc.drop(columns=["Price"])

    # Garantir que todas as feature_columns existam
    for c in feature_columns:
        if c not in df_enc.columns:
            df_enc[c] = 0

    X = df_enc[feature_columns]
    preds = model.predict(X)
    return {"predictions": preds.tolist()}


@app.get("/health")
def health():
    return {"status": "ok"}
