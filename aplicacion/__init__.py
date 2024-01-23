from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://baironbd:Baironbd1@cluster0.7b4ba4z.mongodb.net/DatosEscobilla?retryWrites=true&w=majority'
mongo = PyMongo(app)
CORS(app)

from aplicacion.routes import data_routes, prediction_routes