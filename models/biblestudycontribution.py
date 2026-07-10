from datetime import datetime

from db import db


class BibleStudyContributionModel(db.Model):
    __tablename__ = "bible_study_contributions"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=True)

    insight = db.Column(db.Text, nullable=False)

    approved = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Bible Study
    bible_study_id = db.Column(
        db.Integer,
        db.ForeignKey("bible_studies.id"),
        nullable=False
    )

    bible_study_attr = db.relationship(
        "BibleStudyModel",
        back_populates="contributions_attr",
        cascade="all, delete"
    )

    # Contributor
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    user_attr = db.relationship(
        "UserModel",
        back_populates="study_contributions_attr",
        cascade="all, delete"
    )
