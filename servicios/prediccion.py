import joblib
import numpy as np

def predict(doc_dict):
    dataarray = [
        doc_dict['Rain'],
        doc_dict['Temperature'],
        doc_dict['RH'],
        doc_dict['DewPoint'],
        doc_dict['WindSpeed'],
        doc_dict['GustSpeed'],
        doc_dict['WindDirection'],
        doc_dict['SEVERIDAD']
    ]

    model = joblib.load("servicios/model.pkl")
    X_test = np.array([dataarray])
    prediction = model.predict(X_test).tolist()

    return prediction[0]
