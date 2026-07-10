from datetime import datetime

from db import db


class TestimonyModel(db.Model):
    __tablename__ = "testimonies"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    story = db.Column(db.Text, nullable=False)

    scripture = db.Column(db.String(255), nullable=True)

    published = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

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

    # Foreign Key
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # Relationship
    user_attr = db.relationship(
        "UserModel",
        back_populates="testimonies_attr",
        cascade="all, delete"
    )
    
