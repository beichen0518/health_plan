from flask import Flask
from flask_restful import Api
from src.app.index import Index
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@47.98.172.171/health_plan"
app.config["SQLALCHEMY_POOL_SIZE"] = 10
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1200

db = SQLAlchemy(app)


api.add_resource(Index, "/")




