# app.py
from flask import jsonify
from aplicacion import app
from dominio.data_base import get_latest_data

@app.route('/data', methods=['GET'])
def alldata():
    data = []
    doc_dict = get_latest_data()

    if doc_dict:
        data.append(doc_dict)

    return jsonify(data)
