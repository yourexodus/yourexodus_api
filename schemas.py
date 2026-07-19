from marshmallow import Schema, fields


# =====================================================
# USER
# =====================================================

class PlainUserSchema(Schema):

    id = fields.Int(dump_only=True)

    username = fields.Str(required=True)

    email = fields.Email(required=True)


# Used when registering a new user
class UserSchema(PlainUserSchema):

    password = fields.Str(
        required=True,
        load_only=True
    )

    journals = fields.List(
        fields.Nested("PlainJournalSchema"),
        attribute="journal_attr",
        dump_only=True
    )

    prayers = fields.List(
        fields.Nested("PlainPrayerSchema"),
        attribute="prayers_attr",
        dump_only=True
    )

    testimonies = fields.List(
        fields.Nested("PlainTestimonySchema"),
        attribute="testimonies_attr",
        dump_only=True
    )

    bible_studies = fields.List(
        fields.Nested("PlainBibleStudySchema"),
        attribute="bible_studies_attr",
        dump_only=True
    )

    study_contributions = fields.List(
        fields.Nested("PlainBibleStudyContributionSchema"),
        attribute="study_contributions_attr",
        dump_only=True
    )


# Used ONLY for logging in
class UserLoginSchema(Schema):

    username = fields.Str(
        required=True
    )

    password = fields.Str(
        required=True,
        load_only=True
    )


# =====================================================
# JOURNAL
# =====================================================

class PlainJournalSchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    title = fields.Str(
        required=True
    )

    entry = fields.Str(
        required=True
    )

    scripture = fields.Str(
        allow_none=True
    )

    mood = fields.Str(
        allow_none=True
    )

    is_private = fields.Bool()

    created_at = fields.DateTime(
        dump_only=True
    )

    updated_at = fields.DateTime(
        dump_only=True
    )


class JournalSchema(PlainJournalSchema):

    user_id = fields.Int(
        required=True,
        load_only=True
    )

    user = fields.Nested(
        PlainUserSchema,
        attribute="user_attr",
        dump_only=True
    )



# =====================================================
# PRAYER
# =====================================================

class PlainPrayerSchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    title = fields.Str(
        required=True
    )

    request = fields.Str(
        required=True
    )

    status = fields.Str()

    answered = fields.Bool()

    answered_date = fields.DateTime(
        allow_none=True,
        dump_only=True
    )

    created_at = fields.DateTime(
        dump_only=True
    )


class PrayerSchema(PlainPrayerSchema):

    user_id = fields.Int(
        required=True,
        load_only=True
    )

    user = fields.Nested(
        PlainUserSchema,
        attribute="user_attr",
        dump_only=True
    )



# =====================================================
# TESTIMONY
# =====================================================

class PlainTestimonySchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    title = fields.Str(
        required=True
    )

    story = fields.Str(
        required=True
    )

    scripture = fields.Str(
        allow_none=True
    )

    published = fields.Bool()

    approved = fields.Bool()


class TestimonySchema(PlainTestimonySchema):

    user_id = fields.Int(
        required=True,
        load_only=True
    )

    user = fields.Nested(
        PlainUserSchema,
        attribute="user_attr",
        dump_only=True
    )



# =====================================================
# BIBLE STUDY
# =====================================================

class PlainBibleStudySchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    title = fields.Str(
        required=True
    )

    scripture = fields.Str(
        required=True
    )

    summary = fields.Str(
        allow_none=True
    )

    content = fields.Str(
        required=True
    )

    published = fields.Bool()

    created_at = fields.DateTime(
        dump_only=True
    )

    updated_at = fields.DateTime(
        dump_only=True
    )


class BibleStudySchema(PlainBibleStudySchema):

    category_id = fields.Int(
        required=True,
        load_only=True
    )

    user_id = fields.Int(
        required=True,
        load_only=True
    )


    category = fields.Nested(
        "PlainCategorySchema",
        attribute="category_attr",
        dump_only=True
    )


    user = fields.Nested(
        PlainUserSchema,
        attribute="user_attr",
        dump_only=True
    )



# =====================================================
# BIBLE STUDY CONTRIBUTION
# =====================================================

class PlainBibleStudyContributionSchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    title = fields.Str(
        allow_none=True
    )

    insight = fields.Str(
        required=True
    )

    approved = fields.Bool()

    created_at = fields.DateTime(
        dump_only=True
    )


class BibleStudyContributionSchema(
    PlainBibleStudyContributionSchema
):

    bible_study_id = fields.Int(
        required=True,
        load_only=True
    )

    user_id = fields.Int(
        required=True,
        load_only=True
    )


    bible_study = fields.Nested(
        PlainBibleStudySchema,
        attribute="bible_study_attr",
        dump_only=True
    )


    user = fields.Nested(
        PlainUserSchema,
        attribute="user_attr",
        dump_only=True
    )



# =====================================================
# CATEGORY
# =====================================================

class PlainCategorySchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    name = fields.Str(
        required=True
    )

    description = fields.Str(
        allow_none=True
    )


class CategorySchema(PlainCategorySchema):

    articles = fields.List(
        fields.Nested("PlainArticleSchema"),
        attribute="articles_attr",
        dump_only=True
    )

    bible_studies = fields.List(
        fields.Nested("PlainBibleStudySchema"),
        attribute="bible_studies_attr",
        dump_only=True
    )



# =====================================================
# ARTICLE
# =====================================================

class PlainArticleSchema(Schema):

    id = fields.Int(
        dump_only=True
    )

    title = fields.Str(
        required=True
    )

    content = fields.Str(
        required=True
    )

    image = fields.Str(
        allow_none=True
    )

    author = fields.Str(
        allow_none=True
    )

    published = fields.Bool()

    created_at = fields.DateTime(
        dump_only=True
    )


class ArticleSchema(PlainArticleSchema):

    category_id = fields.Int(
        required=True,
        load_only=True
    )

    category = fields.Nested(
        PlainCategorySchema,
        attribute="category_attr",
        dump_only=True
    )
