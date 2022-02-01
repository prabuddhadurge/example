from email.policy import default
from django.db import models

# Create your models here.
class Movie(models.Model):

   id = models.CharField(primary_key=True, max_length = 40)
   name = models.CharField(max_length = 50, default='')
   description = models.CharField(max_length = 150, default='')
   release_date = models.DateField()

   class Meta:
      db_table = "movie_data"
