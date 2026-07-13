from db import db


class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # One category can have many articles
    articles_attr = db.relationship(
        "ArticleModel",
        back_populates="category_attr",
        cascade="all, delete"
    )
