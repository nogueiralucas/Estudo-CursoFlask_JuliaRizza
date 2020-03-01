from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configurando banco de dados
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)  # Possibilita usar comando no terminal
manager.add_command('db', MigrateCommand)  # Adiciona comando 'db' e o que ele faz

from app.controllers import default
