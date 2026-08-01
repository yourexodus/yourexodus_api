from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.biblestudy import BibleStudyModel
from schemas import BibleStudySchema

blp = Blueprint(
    "Bible Studies",
    __name__,
    description="Operations on Bible Studies"
)


@blp.route("/bible-studies")
@blp.route("/biblestudies")
class BibleStudyList(MethodView):

    def options(self):
        """Handle CORS preflight requests."""
        return "", 200

    @blp.response(200, BibleStudySchema(many=True))
    def get(self):
        """Fetch all published and draft Bible studies."""
        return BibleStudyModel.query.all()

    @blp.arguments(BibleStudySchema)
    @blp.response(201, BibleStudySchema)
    def post(self, bible_study_data):
        """Create a new Bible study lesson."""
        bible_study = BibleStudyModel(**bible_study_data)

        try:
            db.session.add(bible_study)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while creating the Bible study in the database.")

        return bible_study

@blp.route("/bible-studies/<int:biblestudy_id>")
@blp.route("/biblestudies/<int:biblestudy_id>")
class BibleStudy(MethodView):

    @blp.response(200, BibleStudySchema)
    def get(self, biblestudy_id):
        """Retrieve a specific Bible study by ID."""
        bible_study = BibleStudyModel.query.get_or_404(biblestudy_id)
        return bible_study

    @blp.arguments(BibleStudySchema(partial=True))
    @blp.response(200, BibleStudySchema)
    def put(self, bible_study_data, biblestudy_id):
        """Update an existing Bible study or create a new one with a specific ID."""
        bible_study = BibleStudyModel.query.get(biblestudy_id)

        if bible_study:
            for key, value in bible_study_data.items():
                setattr(bible_study, key, value)
        else:
            bible_study = BibleStudyModel(
                id=biblestudy_id,
                **bible_study_data
            )
            db.session.add(bible_study)

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while updating the Bible study.")

        return bible_study

    def delete(self, biblestudy_id):
        """Delete a Bible study record."""
        bible_study = BibleStudyModel.query.get_or_404(biblestudy_id)

        try:
            db.session.delete(bible_study)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while deleting the Bible study.")

        return {"message": "Bible study deleted successfully."}, 200