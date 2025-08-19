from django.contrib.auth.models import User
from django.db import models
# Models are used as a Database where we can create new Tables, Add Fields and Add
# properties to each field.

# Creating class for Tweet
# Where : Tweet is our Table
# Content is our Column
# and Inside () is the properties
# don't forget to include your apps in settings
# Also, make migrations after dealing with Models
# After creating a superuser, go Import your model to the Admin.py
class Tweet(models.Model):
    #content = models.TextField()
# v The use of ForeignKey is to assign a tweet to a user
#   CASCADE deletes any content related to a deleted object or user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# v Expanding Tweet to CharField to give flexibility to assign max characters instead of TextField
    content = models.CharField(max_length=500)
# v Adding additional Tracking for when a tweet is updated and created
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
# v Updating model to fit user-friendly value
# v Creating Function inside the model
    def __str__(self):
        return str(self.content)
    # ^ This block assigns a string value for each object.
    # for now the title of the tweet would be the tweet itself

