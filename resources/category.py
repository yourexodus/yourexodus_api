```python
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models.category import CategoryModel
from schemas import CategorySchema


blp = Blueprint(
    "Categories",
    __name__,
    description="Operations on categories"
)


# ==========================================
# GET ALL CATEGORIES / CREATE CATEGORY
# ==========================================

@blp.route("/categories")
class CategoryList(MethodView):

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        """
        Retrieve all categories.
        """
        return CategoryModel.query.all()


    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, category_data):
        """
        Create a new category.
        """

        existing_category = CategoryModel.query.filter_by(
            name=category_data["name"]
        ).first()

        if existing_category:
            abort(
                409,
                message="A category with that name already exists."
            )

        category = CategoryModel(
            name=category_data["name"],
            description=category_data.get("description")
        )

        db.session.add(category)
        db.session.commit()

        return category


# ==========================================
# GET / UPDATE / DELETE CATEGORY
# ==========================================

@blp.route("/categories/<int:category_id>")
class Category(MethodView):

    @blp.response(200, CategorySchema)
    def get(self, category_id):
        """
        Retrieve a category by ID.
        """
        return CategoryModel.query.get_or_404(category_id)


    @blp.arguments(CategorySchema(partial=True))
    @blp.response(200, CategorySchema)
    def put(self, category_data, category_id):
        """
        Update a category.
        """

        category = CategoryModel.query.get_or_404(category_id)

        if "name" in category_data:
            existing_category = CategoryModel.query.filter_by(
                name=category_data["name"]
            ).first()

            if existing_category and existing_category.id != category.id:
                abort(
                    409,
                    message="A category with that name already exists."
                )

            category.name = category_data["name"]

        if "description" in category_data:
            category.description = category_data["description"]

        db.session.commit()

        return category


    def delete(self, category_id):
        """
        Delete a category.
        """

        category = CategoryModel.query.get_or_404(category_id)

        db.session.delete(category)
        db.session.commit()

        return {
            "message": "Category deleted successfully."
        }, 200
```
