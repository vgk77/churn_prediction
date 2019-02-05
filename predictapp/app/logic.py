import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler


def preprocess_data(user_json):
    dataset = pd.read_json(user_json)
    dataset['TotalCharges'] = dataset['TotalCharges'].replace(' ', np.nan)
    # Дропаем строки с пропущенными значениями TotalCharges
    dataset = dataset[dataset['TotalCharges'].notnull()]
    dataset = dataset.reset_index()[dataset.columns]

    # переведем в вещественные и целые числа
    dataset['TotalCharges'] = dataset['TotalCharges'].astype(float)
    dataset['MonthlyCharges'] = dataset['MonthlyCharges'].astype(float)
    dataset['tenure'] = dataset['tenure'].astype(int)

    # а здесь наоборот переводим в категориальную переменную (да/нет)
    dataset['SeniorCitizen'] = dataset['SeniorCitizen'].replace(
        {1: 'Yes', 0: 'No'})

    # разделяем колонки на два типа (категориальные и вещественные).
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    categorical_cols = list(set(dataset.columns.values.tolist(
    )) - set(numeric_cols) - set(['Churn', 'customerID']))

    X_number = dataset[numeric_cols]
    X_categ = dataset[categorical_cols]
    # на всякий случай все категориальные приведем к строке
    X_categ = X_categ.astype(str)

    encoder = joblib.load('model_data/encoder.joblib')
    # Преобразуем категориальные переменные к вещественному виду
    X_categ_encoded = encoder.transform(X_categ.T.to_dict().values())

    # нормализуем вещественные признаки
    scaler = StandardScaler()
    # scaler = joblib.load('scaler.joblib')
    scaler.fit(X_number)
    X_number_scaled = scaler.transform(X_number)

    # cконкатенируем по горизонтали категориальные и вещественные фичи 
    # и получим окончательный датасет
    X_finish = np.hstack((X_number_scaled, X_categ_encoded))

    return X_finish


def churn_prediction(preprocessed_df, pkl_model):
    our_model = joblib.load(pkl_model)
    # возвращаем только вероятности отвала
    return our_model.predict_proba(preprocessed_df)[:, 0]
