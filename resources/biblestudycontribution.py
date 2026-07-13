from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models.biblestudycontribution import BibleStudyContributionModel
from schemas import BibleStudyContributionSchema


blp = Blueprint(
    "Bible Study Contributions",
    __name__,
    description="Operations on Bible Study Contributions"
)


@blp.route("/biblestudycontributions")
class BibleStudyContributionList(MethodView):

    @blp.response(200, BibleStudyContributionSchema(many=True))
    def get(self):
        return BibleStudyContributionModel.query.all()

    @blp.arguments(BibleStudyContributionSchema)
    @blp.response(201, BibleStudyContributionSchema)
    def post(self, contribution_data):

        contribution = BibleStudyContributionModel(**contribution_data)

        try:
            db.session.add(contribution)
            db.session.commit()

        except Exception:
            abort(
                500,
                message="An error occurred while creating the contribution."
            )

        return contribution


@blp.route("/biblestudycontributions/<int:contribution_id>")
class BibleStudyContribution(MethodView):

    @blp.response(200, BibleStudyContributionSchema)
    def get(self, contribution_id):

        contribution = BibleStudyContributionModel.query.get_or_404(
            contribution_id
        )

        return contribution


    @blp.arguments(BibleStudyContributionSchema)
    @blp.response(200, BibleStudyContributionSchema)
    def put(self, contribution_data, contribution_id):

        contribution = BibleStudyContributionModel.query.get(
            contribution_id
        )

        if contribution:

            for key, value in contribution_data.items():
                setattr(contribution, key, value)

        else:

            contribution = BibleStudyContributionModel(
                id=contribution_id,
                **contribution_data
            )

            db.session.add(contribution)

        db.session.commit()

        return contribution


    def delete(self, contribution_id):

        contribution = BibleStudyContributionModel.query.get_or_404(
            contribution_id
        )

        db.session.delete(contribution)
        db.session.commit()

        return {
            "message": "Bible study contribution deleted."
        }, 200
