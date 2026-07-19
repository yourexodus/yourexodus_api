import os
from dotenv import load_dotenv
from flask import Flask
from db import db

load_dotenv()

def create_app(db_url=None):

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        db_url
        or os.getenv("DATABASE_URL", "sqlite:///data.db")
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app