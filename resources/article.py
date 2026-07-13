from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models.article import ArticleModel
from schemas import ArticleSchema


blp = Blueprint(
    "Articles",
    __name__,
    description="Operations on Articles"
)


@blp.route("/articles")
class ArticleList(MethodView):

    @blp.response(200, ArticleSchema(many=True))
    def get(self):

        return ArticleModel.query.all()


    @blp.arguments(ArticleSchema)
    @blp.response(201, ArticleSchema)
    def post(self, article_data):

        article = ArticleModel(**article_data)

        try:
            db.session.add(article)
            db.session.commit()

        except Exception:
            abort(
                500,
                message="An error occurred while creating the article."
            )

        return article



@blp.route("/articles/<int:article_id>")
class Article(MethodView):

    @blp.response(200, ArticleSchema)
    def get(self, article_id):

        article = ArticleModel.query.get_or_404(article_id)

        return article


    @blp.arguments(ArticleSchema)
    @blp.response(200, ArticleSchema)
    def put(self, article_data, article_id):

        article = ArticleModel.query.get(article_id)

        if article:

            for key, value in article_data.items():
                setattr(article, key, value)

        else:

            article = ArticleModel(
                id=article_id,
                **article_data
            )

            db.session.add(article)

        db.session.commit()

        return article


    def delete(self, article_id):

        article = ArticleModel.query.get_or_404(article_id)

        db.session.delete(article)
        db.session.commit()

        return {
            "message": "Article deleted."
        }, 200
