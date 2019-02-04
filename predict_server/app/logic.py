import pandas as pd
import numpy as np
# import json
import joblib
# from sklearn.feature_extraction import DictVectorizer as DV
from sklearn.preprocessing import StandardScaler


def preprocess_data(user_json):
    dataset = pd.read_json(user_json)
    dataset['TotalCharges'] = dataset["TotalCharges"].replace(" ", np.nan)
    # Дропаем строки с пропущенными значениями TotalCharges
    dataset = dataset[dataset["TotalCharges"].notnull()]
    dataset = dataset.reset_index()[dataset.columns]

    # переведем в вещественные и целые числа
    dataset["TotalCharges"] = dataset["TotalCharges"].astype(float)
    dataset["MonthlyCharges"] = dataset["MonthlyCharges"].astype(float)
    dataset["tenure"] = dataset["tenure"].astype(int)

    # а здесь наоборот переводим в категориальную переменную (да/нет)
    dataset["SeniorCitizen"] = dataset["SeniorCitizen"].replace(
        {1: "Yes", 0: "No"})

    # разделяем колонки на два типа (категориальные и вещественные). Зависимую переменную преобразуем потом
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    categorical_cols = list(set(dataset.columns.values.tolist(
    )) - set(numeric_cols) - set(['Churn', 'customerID']))

    X_number = dataset[numeric_cols]
    X_categ = dataset[categorical_cols]
    # на всякий случай все категориальные приведем к строке (вроде они и так строки)
    X_categ = X_categ.astype(str)

    # encoder = DV(sparse=False)
    encoder = joblib.load('model_data/encoder.joblib')
    # Преобразуем категориальные переменные к вещественному виду с помощью one hot encoder
    # X_categ_encoded = encoder.fit_transform(X_categ.T.to_dict().values())
    X_categ_encoded = encoder.transform(X_categ.T.to_dict().values())

    # нормализуем вещественные признаки
    scaler = StandardScaler()
    # scaler = joblib.load('scaler.joblib')
    scaler.fit(X_number)
    X_number_scaled = scaler.transform(X_number)

    # теперь можно сконкатенировать по горизонтали категориальные и вещественные фичи и получить окончательный датасет
    X_finish = np.hstack((X_number_scaled, X_categ_encoded))

    return X_finish


def churn_prediction(preprocessed_df, pkl_model):
    # data = json.load(json_data)

    # dataset = pd.io.json.json_normalize(json_data)
    # print(dataset.shape)
    # return str(dataset.shape)

    our_model = joblib.load(pkl_model)
    # df = pd.read_json(user_json)
    return str(our_model.predict_proba(preprocessed_df))
