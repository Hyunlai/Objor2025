from django.db import models

class Jobs(models.Model):
    JobTitle = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    min_offers = models.IntegerField()
    max_offers = models.IntegerField()
    location = models.CharField(max_length=100)

