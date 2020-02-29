from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configurando banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///storage.db"
db = SQLAlchemy(app)

from app.controllers import default
