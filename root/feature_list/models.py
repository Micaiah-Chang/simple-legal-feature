from django.db.models import (
    Model,
    CharField, DateTimeField, TextField, URLField,
)

# (date, description, lead developer, url, title)

# Create your models here.
class FeatureModel(Model):
    # Indexing, as "latest date" and "Range of dates"
    # are commonly used operations
    date = DateTimeField("feature published", db_index=True)
    description = TextField()
    # Features do not necessarily have to be
    # localized to one page, nor even be part of one
    # Maybe needs to be updated to a Many to Many field later
    url = URLField(default="", blank=True)
    # This may turn into a foreign key in the future, if
    # feature searches are needed internally
    lead_developer = CharField(max_length=200)
    # Picking twitter length rules for no  good reason.
    title = CharField(max_length=140)

    def __unicode__(self):
        return u"%s", self.title
