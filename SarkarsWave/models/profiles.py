from mongoengine import Document, StringField, BooleanField, EmbeddedDocument, FloatField, EmbeddedDocumentField, \
    ListField

from utils.helper import current_date


class AboutSelf(EmbeddedDocument):
    total_year_exp = FloatField(default=0.0)
    complete_projects = StringField(default="0")
    no_companies_worked = StringField(default="0")
    desc = StringField(required=True)


class Skills(EmbeddedDocument):
    name = StringField(required=True)
    weight = StringField(default="0")
    type = StringField(required=True)


class Qualification(EmbeddedDocument):
    title = StringField(required=True)
    org = StringField(required=True)
    tenure_from = StringField(required=True)
    tenure_to = StringField(default="Till now")


class Experience(EmbeddedDocument):
    title = StringField(required=True)
    org = StringField(required=True)
    tenure_from = StringField(required=True)
    tenure_to = StringField(default="Till now")


class Services(EmbeddedDocument):
    title = StringField(required=True)
    key_points = ListField(required=True)


class Profiles(Document):
    first_name = StringField(max_length=30, min_length=4, required=True)
    middle_name = StringField(max_length=30, min_length=0, required=False)
    last_name = StringField(max_length=30, min_length=4, required=True)
    title = StringField(min_length=4, required=True)
    title_description = StringField(required=True)
    about_me = EmbeddedDocumentField(AboutSelf, required=True)
    skill_sets = ListField(EmbeddedDocumentField(Skills))
    qualification = ListField(EmbeddedDocumentField(Qualification), required=True)
    experience = ListField(EmbeddedDocumentField(Experience), required=True)
    services_offered = ListField(EmbeddedDocumentField(Services), required=True)
    profile_image = StringField()
    email = StringField(required=True, unique=True)
    github_url = StringField(default="")
    linkedin_url = StringField(default="")
    portfolio_web_url = StringField(default="")
    contact_no = StringField(required=True, unique=True)
    location = StringField(required=True, unique=True)
    timestamp = StringField(max_length=10, default=current_date())
    last_updated = StringField(max_length=10, default=current_date())
    is_active = BooleanField(default=True)
