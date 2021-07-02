from django.db import models
import mongoengine

# Create your models here.

class UserModel(mongoengine.Document):
    userName = mongoengine.StringField(min_length=5, required=True)
    userPass = mongoengine.StringField(min_length=5, required=True)

    def __unicode__(self):
        return self.name