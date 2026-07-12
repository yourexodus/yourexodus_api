import os
from flask import Flask
from flask_smorest import Api

from db import db

# Blueprints
from resources.user import blp as UserBlueprint
from resources.journal import blp as JournalBlueprint
from resources.prayer import blp as PrayerBlueprint
# from resources.testimony import blp as TestimonyBlueprint
# from resources.bible_study import blp as BibleStudyBlueprint
# from resources.bible_study_contribution import blp as BibleStudyContributionBlueprint
# from resources.category import blp as CategoryBlueprint
# from resources.article import blp as ArticleBlueprint

# Models
import models.user
import models.journal
import models.prayer
import models.testimony
import models.biblestudy
import models.biblestudycontribution
import models.category
import models.article


def create_app(db_url=None):
    app = Flask(__name__)

    # -----------------------------
    # API Configuration
    # -----------------------------

    app.config["API_TITLE"] = "Your Exodus REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"

    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # -----------------------------
    # Database
    # -----------------------------

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        db_url
        or os.getenv("DATABASE_URL", "sqlite:///data.db")
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)

    # -----------------------------
    # Register Blueprints
    # -----------------------------

    api.register_blueprint(UserBlueprint)

    # Uncomment as each resource is created.

    api.register_blueprint(JournalBlueprint)
    api.register_blueprint(PrayerBlueprint)
    # api.register_blueprint(TestimonyBlueprint)
    # api.register_blueprint(BibleStudyBlueprint)
    # api.register_blueprint(BibleStudyContributionBlueprint)
    # api.register_blueprint(CategoryBlueprint)
    # api.register_blueprint(ArticleBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        debug=True
    )
