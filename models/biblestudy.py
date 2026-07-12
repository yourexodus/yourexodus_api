from datetime import datetime

from db import db


class BibleStudyModel(db.Model):
    __tablename__ = "bible_studies"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    scripture = db.Column(db.String(255), nullable=False)

    summary = db.Column(db.Text, nullable=True)

    content = db.Column(db.Text, nullable=False)

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

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Category
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    category_attr = db.relationship(
        "CategoryModel",
        back_populates="bible_studies_attr" 
    )

    # Author
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    user_attr = db.relationship(
        "UserModel",
        back_populates="bible_studies_attr" 
    )

    # Community Contributions
    contributions_attr = db.relationship(
        "BibleStudyContributionModel",
        back_populates="bible_study_attr" 
    )
