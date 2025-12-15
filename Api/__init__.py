from flask import Flask
from flask_restful import Api
from .extensions import database, cors
from .instance.config import DevelopmentConfig

from .routes import registerResources

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_app():
    app = Flask(
        __name__,
        instance_path=os.path.join(BASE_DIR, "instance"),
        instance_relative_config=True
    )
    app.config.from_object(DevelopmentConfig)

    cors.init_app(app)

    db_path = os.path.join(app.instance_path, "data.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    os.makedirs(app.instance_path, exist_ok=True)

    database.init_app(app)

    api = Api(app)

    # IMPORTANT: register resources AFTER init
    registerResources(api)

    return app
