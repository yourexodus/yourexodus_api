from datetime import datetime
from db import db  # Assuming your db instance is imported like this


class JournalModel(db.Model):
    __tablename__ = "journals"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    entry = db.Column(db.Text, nullable=False)
    scripture = db.Column(db.String(255), nullable=True)
    mood = db.Column(db.String(50), nullable=True)
    is_private = db.Column(db.Boolean, default=True, nullable=False)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Foreign Key linking to the user
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False
    )

    # Optional: If you have a UserModel, you'll want to define the relationship
    user_attr = db.relationship("UserModel", back_populates="journal_attr")
