from datetime import datetime, timedelta
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.prayer import PrayerModel
from schemas import PrayerSchema


blp = Blueprint(
    "prayers",
    __name__,
    description="Operations on prayer entries"
)

# PART I
# ✅ Blueprint setup
# ✅ Create prayer (POST /prayers)
# ✅ Get all prayers (GET /prayers)
# ✅ Get one prayer (GET /prayers/<prayer_id>)
# ✅ Update prayer (PUT /prayers/<prayer_id>)
# ✅ Delete prayer (DELETE /prayers/<prayer_id>)
# =====================================================
# CREATE, GET ALL prayerS
# =====================================================

@blp.route("/prayers")
class PrayerList(MethodView):

    @blp.response(200, PrayerSchema(many=True))
    def get(self):
        """
        Get all prayer entries
        """
        return PrayerModel.query.all()


    @blp.arguments(PrayerSchema)
    @blp.response(201, PrayerSchema)
    def post(self, prayer_data):
        """
        Create a new prayer entry
        """

        prayer = PrayerModel(**prayer_data)

        try:
            db.session.add(prayer)
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            abort(
                500,
                message="An error occurred while creating the prayer."
            )

        return prayer


# =====================================================
# GET ONE, UPDATE, DELETE prayer
# =====================================================

@blp.route("/prayers/<int:prayer_id>")
class Prayer(MethodView):

    @blp.response(200, PrayerSchema)
    def get(self, prayer_id):
        """
        Get a prayer entry by ID
        """

        prayer = PrayerModel.query.get(prayer_id)

        if not prayer:
            abort(
                404,
                message="prayer not found."
            )

        return prayer


    @blp.arguments(PrayerSchema)
    @blp.response(200, PrayerSchema)
    def put(self, prayer_data, prayer_id):
        """
        Update an existing prayer entry
        """

        prayer = PrayerModel.query.get(prayer_id)

        if not prayer:
            abort(
                404,
                message="prayer not found."
            )


        prayer.title = prayer_data.get(
                "title",
                prayer.title
        )

        prayer.prayer = prayer_data.get(
                "prayer",
                prayer.prayer
        )

        prayer.scripture = prayer_data.get(
                "scripture",
                prayer.scripture
        )

        prayer.answered = prayer_data.get(
                "answered",
                prayer.answered
        )


        try:
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            abort(
                500,
                message="An error occurred while updating the prayer."
            )

        return prayer


    @blp.response(200)
    def delete(self, prayer_id):
        """
        Delete a prayer entry
        """

        prayer = PrayerModel.query.get(prayer_id)

        if not prayer:
            abort(
                404,
                message="prayer not found."
            )


        try:
            db.session.delete(prayer)
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            abort(
                500,
                message="An error occurred while deleting the prayer."
            )
        return {
            "message": "Prayer deleted successfully."
        }


# PART 2
# ✅ Search prayers by keyword
# ✅ Search prayers by date range
# ✅ Swagger documentation
# ✅ SQLAlchemy filtering

    # =====================================================
# SEARCH prayerS BY KEYWORD
# =====================================================

@blp.route("/prayers/search")
class PrayerSearch(MethodView):

    @blp.response(200, PrayerSchema(many=True))
    def get(self):
        """
        Search prayers by keyword.

        Example:
        /prayers/search?keyword=faith
        """

        keyword = (
            request.args.get("keyword")
        )

        if not keyword:
            abort(
                400,
                message="Keyword is required."
            )


        search_term = f"%{keyword}%"


        prayers = PrayerModel.query.filter(
            db.or_(
                PrayerModel.title.ilike(search_term),
                PrayerModel.prayer.ilike(search_term),
                PrayerModel.scripture.ilike(search_term)
            )
        ).all()


        return prayers



# =====================================================
# SEARCH prayerS BY DATE RANGE
# =====================================================

@blp.route("/prayers/date-range")
class PrayerDateRangeSearch(MethodView):

    @blp.response(200, PrayerSchema(many=True))
    def get(self):
        """
        Search prayers by creation date range.

        Example:
        /prayers/date-range?start=2026-01-01&end=2026-12-31
        """


        start_date = request.args.get(
            "start"
        )

        end_date = request.args.get(
            "end"
        )


        if not start_date or not end_date:
            abort(
                400,
                message="Both start and end dates are required."
            )


        try:
            start = datetime.strptime(
                start_date,
                "%Y-%m-%d"
            )

            end = datetime.strptime(
                end_date,
                "%Y-%m-%d"
            )

        except ValueError:
            abort(
                400,
                message="Date format must be YYYY-MM-DD."
            )

        # Make end date inclusive
        end = end + timedelta(days=1)

        prayers = PrayerModel.query.filter(
            PrayerModel.created_at >= start,
            PrayerModel.created_at < end
        ).all()


        return prayers

 
