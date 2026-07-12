from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.journal import JournalModel
from schemas import JournalSchema


blp = Blueprint(
    "Journals",
    __name__,
    description="Operations on journal entries"
)

# PART I
# ✅ Blueprint setup
# ✅ Create journal (POST /journals)
# ✅ Get all journals (GET /journals)
# ✅ Get one journal (GET /journals/<journal_id>)
# ✅ Update journal (PUT /journals/<journal_id>)
# ✅ Delete journal (DELETE /journals/<journal_id>)
# =====================================================
# CREATE, GET ALL JOURNALS
# =====================================================

@blp.route("/journals")
class JournalList(MethodView):

    @blp.response(200, JournalSchema(many=True))
    def get(self):
        """
        Get all journal entries
        """
        return JournalModel.query.all()


    @blp.arguments(JournalSchema)
    @blp.response(201, JournalSchema)
    def post(self, journal_data):
        """
        Create a new journal entry
        """

        journal = JournalModel(**journal_data)

        try:
            db.session.add(journal)
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            abort(
                500,
                message="An error occurred while creating the journal."
            )

        return journal


# =====================================================
# GET ONE, UPDATE, DELETE JOURNAL
# =====================================================

@blp.route("/journals/<int:journal_id>")
class Journal(MethodView):

    @blp.response(200, JournalSchema)
    def get(self, journal_id):
        """
        Get a journal entry by ID
        """

        journal = JournalModel.query.get(journal_id)

        if not journal:
            abort(
                404,
                message="Journal not found."
            )

        return journal


    @blp.arguments(JournalSchema)
    @blp.response(200, JournalSchema)
    def put(self, journal_data, journal_id):
        """
        Update an existing journal entry
        """

        journal = JournalModel.query.get(journal_id)

        if not journal:
            abort(
                404,
                message="Journal not found."
            )


        journal.title = journal_data.get(
            "title",
            journal.title
        )

        journal.entry = journal_data.get(
            "entry",
            journal.entry
        )

        journal.scripture = journal_data.get(
            "scripture",
            journal.scripture
        )

        journal.mood = journal_data.get(
            "mood",
            journal.mood
        )

        journal.is_private = journal_data.get(
            "is_private",
            journal.is_private
        )


        try:
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            abort(
                500,
                message="An error occurred while updating the journal."
            )

        return journal


    @blp.response(200)
    def delete(self, journal_id):
        """
        Delete a journal entry
        """

        journal = JournalModel.query.get(journal_id)

        if not journal:
            abort(
                404,
                message="Journal not found."
            )


        try:
            db.session.delete(journal)
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            abort(
                500,
                message="An error occurred while deleting the journal."
            )


# PART 2
# ✅ Search journals by keyword
# ✅ Search journals by date range
# ✅ Swagger documentation
# ✅ SQLAlchemy filtering

    # =====================================================
# SEARCH JOURNALS BY KEYWORD
# =====================================================

@blp.route("/journals/search")
class JournalSearch(MethodView):

    @blp.response(200, JournalSchema(many=True))
    def get(self):
        """
        Search journals by keyword.

        Example:
        /journals/search?keyword=faith
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


        journals = JournalModel.query.filter(
            db.or_(
                JournalModel.title.ilike(search_term),
                JournalModel.entry.ilike(search_term),
                JournalModel.scripture.ilike(search_term)
            )
        ).all()


        return journals



# =====================================================
# SEARCH JOURNALS BY DATE RANGE
# =====================================================

@blp.route("/journals/date-range")
class JournalDateRangeSearch(MethodView):

    @blp.response(200, JournalSchema(many=True))
    def get(self):
        """
        Search journals by creation date range.

        Example:
        /journals/date-range?start=2026-01-01&end=2026-12-31
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


        journals = JournalModel.query.filter(
            JournalModel.created_at >= start,
            JournalModel.created_at <= end
        ).all()


        return journals

 
