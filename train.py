import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler


def prepare_data(df, target_col: str = "Price", test_size: float = 0.2, random_state: int = 42):
    """Prepara X e y e faz split em treino/teste.

    Retorna: X_train, X_test, y_train, y_test
    """
    if target_col not in df.columns:
        raise ValueError(f"Coluna alvo '{target_col}' não existe no DataFrame")

    y = df[target_col]
    X = df.drop(target_col, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


def scale_data(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def train_model(X_train, y_train, n_estimators: int = 100, random_state: int = 42):
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state, n_jobs=-1)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    return {"r2": r2, "mae": mae}


if __name__ == "__main__":
    print("Este módulo contém funções de preparação, treino e avaliação de modelos.")
