from flask.views import MethodView
from flask_smorest import Blueprint, abort
# Removed all JWT imports like create_access_token, jwt_required, etc.
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema
# Removed: from blocklist import BLOCKLIST

blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            # JWT Token creation logic removed:
            # access_token = create_access_token(identity=user.id, fresh=True)
            # refresh_token = create_refresh_token(user.id)
            # return {"access_token": access_token, "refresh_token": refresh_token}, 200
            
            # Simple success message returned instead:
            return {"message": "Logged in successfully."}, 200

        abort(401, message="Invalid credentials.")


# Removed the entire UserLogout resource class.

# Removed the entire TokenRefresh resource class.


@blp.route("/user/<int:user_id>")
class User(MethodView):
    """
    This resource can be useful when testing our Flask app.
    It is now public (no authentication required).
    """

    # Removed @jwt_required() decorator
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    # Removed @jwt_required() decorator
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200