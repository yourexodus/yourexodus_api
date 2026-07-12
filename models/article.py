from datetime import datetime

from db import db


class ArticleModel(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    image = db.Column(db.String(255), nullable=True)

    author = db.Column(db.String(100), nullable=True)

    published = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Foreign Key
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    # Relationship
    category_attr = db.relationship(
        "CategoryModel" 
        
    )
