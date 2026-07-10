from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

 # Relationships
    journal_attr = db.relationship(
        "JournalModel",
        back_populates="user_attr",
        cascade="all, delete-orphan"
    )

    prayers_attr = db.relationship(
        "PrayerModel",
        back_populates="user_attr",
        cascade="all, delete-orphan"
    )

     
    testimonies_attr = db.relationship(
        "TestimonyModel",
        back_populates="user_attr",
        cascade="all, delete"
    )



    study_contributions_attr = db.relationship(
        "BibleStudyContributionModel",
        back_populates="user_attr",
        cascade="all, delete"
    )

    bible_studies_attr = db.relationship(
        "BibleStudyModel",
        back_populates="user_attr",
        cascade="all, delete"
    )
