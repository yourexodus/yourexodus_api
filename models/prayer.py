from datetime import datetime

from db import db


class PrayerModel(db.Model):

    __tablename__ = "prayers"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    title = db.Column(
        db.String(150),
        nullable=False
    )


    request = db.Column(
        db.Text,
        nullable=False
    )


    # Prayer category
    category = db.Column(
        db.String(50),
        nullable=True
    )


    # Privacy setting
    is_private = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )


    # AI generated prayer response
    ai_response = db.Column(
        db.Text,
        nullable=True
    )


    # Status can hold "New", "Praying", or "Answered"
    status = db.Column(
        db.String(20),
        default="New",
        nullable=False
    )


    answered = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )


    # Date prayer was answered
    answered_date = db.Column(
        db.DateTime,
        nullable=True
    )


    # Created timestamp
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )


    # Foreign Key linking to the user
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=False,
        nullable=False
    )


    # Link back to UserModel
    user_attr = db.relationship(
        "UserModel",
        back_populates="prayers_attr"
    )