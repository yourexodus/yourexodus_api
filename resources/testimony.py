from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models.testimony import TestimonyModel
from schemas import TestimonySchema

blp = Blueprint(
    "Testimonies",
    __name__,
    description="Operations on Testimonies"
)


@blp.route("/testimonies")
class TestimonyList(MethodView):

    @blp.response(200, TestimonySchema(many=True))
    def get(self):
        return TestimonyModel.query.all()

    @blp.arguments(TestimonySchema)
    @blp.response(201, TestimonySchema)
    def post(self, testimony_data):
        testimony = TestimonyModel(**testimony_data)

        try:
            db.session.add(testimony)
            db.session.commit()
        except Exception:
            abort(500, message="An error occurred while creating the testimony.")

        return testimony


@blp.route("/testimonies/<int:testimony_id>")
class Testimony(MethodView):

    @blp.response(200, TestimonySchema)
    def get(self, testimony_id):
        testimony = TestimonyModel.query.get_or_404(testimony_id)
        return testimony

    @blp.arguments(TestimonySchema)
    @blp.response(200, TestimonySchema)
    def put(self, testimony_data, testimony_id):
        testimony = TestimonyModel.query.get(testimony_id)

        if testimony:
            for key, value in testimony_data.items():
                setattr(testimony, key, value)
        else:
            testimony = TestimonyModel(
                id=testimony_id,
                **testimony_data
            )
            db.session.add(testimony)

        db.session.commit()
        return testimony

    def delete(self, testimony_id):
        testimony = TestimonyModel.query.get_or_404(testimony_id)

        db.session.delete(testimony)
        db.session.commit()

        return {"message": "Testimony deleted."}, 200
