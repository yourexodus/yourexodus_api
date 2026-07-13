from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models.biblestudy import BibleStudyModel
from schemas import BibleStudySchema

blp = Blueprint(
    "Bible Studies",
    __name__,
    description="Operations on Bible Studies"
)


@blp.route("/biblestudies")
class BibleStudyList(MethodView):

    @blp.response(200, BibleStudySchema(many=True))
    def get(self):
        return BibleStudyModel.query.all()

    @blp.arguments(BibleStudySchema)
    @blp.response(201, BibleStudySchema)
    def post(self, bible_study_data):
        bible_study = BibleStudyModel(**bible_study_data)

        try:
            db.session.add(bible_study)
            db.session.commit()
        except Exception:
            abort(500, message="An error occurred while creating the Bible study.")

        return bible_study


@blp.route("/biblestudies/<int:biblestudy_id>")
class BibleStudy(MethodView):

    @blp.response(200, BibleStudySchema)
    def get(self, biblestudy_id):
        bible_study = BibleStudyModel.query.get_or_404(biblestudy_id)
        return bible_study

    @blp.arguments(BibleStudySchema)
    @blp.response(200, BibleStudySchema)
    def put(self, bible_study_data, biblestudy_id):
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

        db.session.commit()
        return bible_study

    def delete(self, biblestudy_id):
        bible_study = BibleStudyModel.query.get_or_404(biblestudy_id)

        db.session.delete(bible_study)
        db.session.commit()

        return {"message": "Bible study deleted."}, 200
