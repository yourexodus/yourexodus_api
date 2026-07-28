import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.prayer import PrayerModel
from schemas import PrayerSchema

from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



blp = Blueprint(
    "prayers",
    __name__,
    description="Operations on prayer entries"
)



# =====================================================
# AI PRAYER GENERATOR
# =====================================================

def generate_ai_prayer(request_text, category):

    try:

        prompt = f"""
        Write a compassionate Christian prayer.

        Prayer request:
        {request_text}

        Category:
        {category}

        Include:
        - encouragement
        - scripture
        - hope
        - a personal prayer
        """


        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )


        return response.text


    except Exception:

        return None




# =====================================================
# CREATE AND GET ALL PRAYERS
# =====================================================

@blp.route("/prayers")
class PrayerList(MethodView):


    @blp.response(200, PrayerSchema(many=True))
    def get(self):

        return PrayerModel.query.order_by(
            PrayerModel.created_at.desc()
        ).all()



    @blp.arguments(PrayerSchema)
    @blp.response(201, PrayerSchema)
    def post(self, prayer_data):

        prayer = PrayerModel(

            title=prayer_data["title"],

            request=prayer_data["request"],

            user_id=prayer_data["user_id"],

            category=prayer_data.get(
                "category"
            ),

            is_private=prayer_data.get(
                "is_private",
                True
            )

        )


        prayer.ai_response = generate_ai_prayer(
            prayer.request,
            prayer.category
        )


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
# GET ONE, UPDATE, DELETE PRAYER
# =====================================================

@blp.route("/prayers/<int:prayer_id>")
class Prayer(MethodView):


    @blp.response(200, PrayerSchema)
    def get(self, prayer_id):

        prayer = PrayerModel.query.get(
            prayer_id
        )


        if not prayer:

            abort(
                404,
                message="Prayer not found."
            )


        return prayer




    @blp.arguments(PrayerSchema)
    @blp.response(200, PrayerSchema)
    def put(self, prayer_data, prayer_id):

        prayer = PrayerModel.query.get(
            prayer_id
        )


        if not prayer:

            abort(
                404,
                message="Prayer not found."
            )


        prayer.title = prayer_data.get(
            "title",
            prayer.title
        )


        prayer.request = prayer_data.get(
            "request",
            prayer.request
        )


        prayer.category = prayer_data.get(
            "category",
            prayer.category
        )


        prayer.is_private = prayer_data.get(
            "is_private",
            prayer.is_private
        )


        prayer.answered = prayer_data.get(
            "answered",
            prayer.answered
        )


        if prayer.answered:

            prayer.status = "Answered"


            if prayer.answered_date is None:

                prayer.answered_date = datetime.utcnow()


        else:

            prayer.status = "New"

            prayer.answered_date = None


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

        prayer = PrayerModel.query.get(
            prayer_id
        )


        if not prayer:

            abort(
                404,
                message="Prayer not found."
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




# =====================================================
# SEARCH PRAYERS BY KEYWORD
# =====================================================

@blp.route("/prayers/search")
class PrayerSearch(MethodView):


    @blp.response(200, PrayerSchema(many=True))
    def get(self):

        keyword = request.args.get(
            "keyword"
        )


        if not keyword:

            abort(
                400,
                message="Keyword is required."
            )


        search_term = f"%{keyword}%"


        prayers = PrayerModel.query.filter(

            db.or_(

                PrayerModel.title.ilike(
                    search_term
                ),

                PrayerModel.request.ilike(
                    search_term
                ),

                PrayerModel.category.ilike(
                    search_term
                )

            )

        ).order_by(

            PrayerModel.created_at.desc()

        ).all()


        return prayers




# =====================================================
# SEARCH PRAYERS BY DATE RANGE
# =====================================================

@blp.route("/prayers/date-range")
class PrayerDateRangeSearch(MethodView):


    @blp.response(200, PrayerSchema(many=True))
    def get(self):

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


        end = end + timedelta(
            days=1
        )


        prayers = PrayerModel.query.filter(

            PrayerModel.created_at >= start,

            PrayerModel.created_at < end

        ).order_by(

            PrayerModel.created_at.desc()

        ).all()


        return prayers