# database.py
from flask_pymongo import PyMongo
from bson import json_util
from aplicacion import app

mongo = PyMongo(app)

def get_latest_data():
    doc = mongo.db.data.find_one(sort=[('_id', -1)])
    if doc:
        doc_dict = json_util.loads(json_util.dumps(doc))
        return {
            '_id': str(doc_dict['_id']),
            'Rain': doc_dict['Rain'],
            'Temperature': doc_dict['Temperature'],
            'RH': doc_dict['RH'],
            'DewPoint': doc_dict['DewPoint'],
            'WindSpeed': doc_dict['WindSpeed'],
            'GustSpeed': doc_dict['GustSpeed'],
            'WindDirection': doc_dict['WindDirection'],
            'SEVERIDAD': doc_dict['SEVERIDAD'],
            'INCIDENCIA': doc_dict['INCIDENCIA']
        }
    else:
        return None
