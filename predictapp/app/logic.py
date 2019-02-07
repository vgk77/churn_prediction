import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler


def preprocess_data(user_json):
    dataset = pd.DataFrame(user_json)
    #dataset = pd.read_json(user_json)
    # разделяем колонки на два типа (категориальные и вещественные).
    numeric_cols = ['tenure', 'monthly_charges', 'total_charges']
    categorical_cols = list(set(dataset.columns.values.tolist(
    )) - set(numeric_cols) - set(['churn', 'customer_id']))

    X_number = dataset[numeric_cols]
    X_categ = dataset[categorical_cols]

    # Преобразуем категориальные переменные к вещественному виду
    encoder = joblib.load('model_data/encoder.joblib')
    X_categ_encoded = encoder.transform(X_categ.T.to_dict().values())

    # нормализуем вещественные признаки
    scaler = joblib.load('model_data/scaler.joblib')
    X_number_scaled = scaler.transform(X_number)

    # cконкатенируем по горизонтали категориальные и вещественные фичи 
    # и получим окончательный датасет
    X_finish = np.hstack((X_number_scaled, X_categ_encoded))

    return X_finish


def churn_prediction(preprocessed_df, pkl_model):
    our_model = joblib.load(pkl_model)
    # возвращаем только вероятности отвала
    return our_model.predict_proba(preprocessed_df)[:, 0]
