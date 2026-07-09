from datetime import datetime
from db import db


class PrayerModel(db.Model):
    __tablename__ = "prayers"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    request = db.Column(db.Text, nullable=False)

    # Status can hold "New", "Praying", or "Answered"
    status = db.Column(db.String(20), default="New", nullable=False)
    answered = db.Column(db.Boolean, default=False, nullable=False)

    # Timestamps
    answered_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Foreign Key linking to the user
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False
    )

    # Optional: If you want to link it to your UserModel
    user_attr = db.relationship("UserModel", back_populates="prayers_attr")
