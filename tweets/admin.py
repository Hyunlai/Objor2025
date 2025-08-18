from django.contrib import admin

# Register your models here.
# Import your models
from .models import *

admin.site.register(Tweet)

#Admin tweet edits : To make it not "Tweet object (1)" go update your model.