from marshmallow import Schema, fields


# =====================================================
# USER
# =====================================================

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)


class UserSchema(PlainUserSchema):
    password = fields.Str(required=True, load_only=True)

    journals = fields.List(
        fields.Nested("PlainJournalSchema"),
	attribute="journal_attr",
        dump_only=True
    )

    prayers = fields.List(
        fields.Nested("PlainPrayerSchema"),
        dump_only=True
    )

    testimonies = fields.List(
        fields.Nested("PlainTestimonySchema"),
        dump_only=True
    )

    bible_studies = fields.List(
        fields.Nested("PlainBibleStudySchema"),
        dump_only=True
    )

    study_contributions = fields.List(
        fields.Nested("PlainBibleStudyContributionSchema"),
        dump_only=True
    )


# =====================================================
# JOURNAL
# =====================================================

class PlainJournalSchema(Schema):
    id = fields.Int(dump_only=True)

    title = fields.Str(required=True)
    entry = fields.Str(required=True)
    scripture = fields.Str(allow_none=True)
    mood = fields.Str(allow_none=True)

    is_private = fields.Bool(load_default=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)




class JournalSchema(PlainJournalSchema):
    user_id = fields.Int(required=True, load_only=True)

    user = fields.Nested(
        PlainUserSchema,
	attribute="user_attr",
        dump_only=True
    )


# =====================================================
# PRAYER
# =====================================================

class PlainPrayerSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    prayer = fields.Str(required=True)
    scripture = fields.Str()
    answered = fields.Bool()


class PrayerSchema(PlainPrayerSchema):
    user_id = fields.Int(required=True, load_only=True)

    user = fields.Nested(
        PlainUserSchema,
        dump_only=True
    )


# =====================================================
# TESTIMONY
# =====================================================

class PlainTestimonySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    testimony = fields.Str(required=True)


class TestimonySchema(PlainTestimonySchema):
    user_id = fields.Int(required=True, load_only=True)

    user = fields.Nested(
        PlainUserSchema,
        dump_only=True
    )


# =====================================================
# BIBLE STUDY
# =====================================================

class PlainBibleStudySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    scripture = fields.Str()


class BibleStudySchema(PlainBibleStudySchema):
    user_id = fields.Int(required=True, load_only=True)

    user = fields.Nested(
        PlainUserSchema,
        dump_only=True
    )


# =====================================================
# BIBLE STUDY CONTRIBUTION
# =====================================================

class PlainBibleStudyContributionSchema(Schema):
    id = fields.Int(dump_only=True)
    contribution = fields.Str(required=True)


class BibleStudyContributionSchema(PlainBibleStudyContributionSchema):
    user_id = fields.Int(required=True, load_only=True)
    bible_study_id = fields.Int(required=True, load_only=True)

    user = fields.Nested(
        PlainUserSchema,
        dump_only=True
    )

    bible_study = fields.Nested(
        PlainBibleStudySchema,
        dump_only=True
    )


# =====================================================
# CATEGORY
# =====================================================

class PlainCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()


class CategorySchema(PlainCategorySchema):

    articles = fields.List(
        fields.Nested("PlainArticleSchema"),
        dump_only=True
    )


# =====================================================
# ARTICLE
# =====================================================

class PlainArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    scripture = fields.Str()
    image_url = fields.Str()


class ArticleSchema(PlainArticleSchema):

    category_id = fields.Int(required=True, load_only=True)

    category = fields.Nested(
        PlainCategorySchema,
        dump_only=True
    )

