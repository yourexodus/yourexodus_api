import os
from flask import Flask
from flask_smorest import Api
# REMOVED: Imports related to JWTManager and Migrate

from db import db
# REMOVED: from blocklist import BLOCKLIST

from resources.user import blp as UserBlueprint
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint

# Ensure models are imported at top-level for SQLAlchemy
import models.user
import models.item
import models.store
import models.tag

import logging

def create_app(db_url=None):
    app = Flask(__name__)
    
    # --- API Configuration ---
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    # --- Database Configuration ---
    # Using SQLite as the default for now
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    
    db.init_app(app)
    
    # === CRITICAL FIX: AUTOMATIC TABLE CREATION ===
    # This ensures tables (like 'users') are created on startup if they don't exist, 
    # resolving the "no such table" error.
    with app.app_context():
        db.create_all()
    # ==============================================
    
    api = Api(app)

    # REMOVED: All JWT initialization and callback functions.
    
    # --- Register Blueprints ---
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    return app

# REMOVED: The make_migrations_app() function

# Local development only (This part will not run on Render/Gunicorn)
if __name__ == "__main__":
    app = create_app()
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 10000)))