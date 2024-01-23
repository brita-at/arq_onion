from flask import jsonify, request
from flask_pymongo import PyMongo
from bson import json_util

from aplicacion import app
from servicios.prediccion import predict
from dominio.data_base import get_latest_data

mongo = PyMongo(app)

@app.route('/predecir', methods=['GET'])
def dataarray(): 
    doc_dict = get_latest_data()

    if doc_dict:
        prediction = predict(doc_dict)

        if prediction == 1:
            return jsonify('Cultivo infectado, se recomienda acción rápida')
        else:
            return jsonify('Cultivo sano, todo tranquilo')
    else:
        return jsonify('No se encontraron datos para hacer la predicción.')