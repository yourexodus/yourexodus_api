from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint(
    "Users",
    __name__,
    description="Operations on users."
)


# =====================================================
# Register User
# =====================================================

@blp.route("/users/register")
class UserRegister(MethodView):

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        """
        Register a new user.
        """

        if UserModel.query.filter_by(
            username=user_data["username"]
        ).first():
            abort(
                409,
                message="A user with that username already exists."
            )

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(
                user_data["password"]
            )
        )

        db.session.add(user)
        db.session.commit()

        return user


# =====================================================
# Login User
# =====================================================

@blp.route("/users/login")
class UserLogin(MethodView):

    @blp.arguments(UserSchema)
    def post(self, user_data):
        """
        Authenticate a user.
        """

        user = UserModel.query.filter_by(
            username=user_data["username"]
        ).first()

        if not user:
            abort(
                401,
                message="Invalid username or password."
            )

        if not pbkdf2_sha256.verify(
            user_data["password"],
            user.password
        ):
            abort(
                401,
                message="Invalid username or password."
            )

        return {
            "message": "Login successful."
        }, 200


# =====================================================
# User Resource
# =====================================================

@blp.route("/users/<int:user_id>")
class User(MethodView):

    @blp.response(200, UserSchema)
    def get(self, user_id):
        """
        Retrieve a user by ID.
        """

        return UserModel.query.get_or_404(user_id)


    def delete(self, user_id):
        """
        Delete a user.
        """

        user = UserModel.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return {
            "message": "User deleted successfully."
        }, 200


    @blp.arguments(UserSchema(partial=True))
    @blp.response(200, UserSchema)
    def put(self, user_data, user_id):
        """
        Update a user's information.
        """

        user = UserModel.query.get_or_404(user_id)

        if "username" in user_data:
            existing_user = UserModel.query.filter_by(
                username=user_data["username"]
            ).first()

            if existing_user and existing_user.id != user.id:
                abort(
                    409,
                    message="Username already exists."
                )

            user.username = user_data["username"]

        if "password" in user_data:
            user.password = pbkdf2_sha256.hash(
                user_data["password"]
            )

        db.session.commit()

        return user
