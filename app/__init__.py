from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
app.config.from_object(app.config)
CORS(app)

from app import routesObtener
from app import routesAgregar
from app import routesActualizar
from app import routesEliminar
from app import consultas
