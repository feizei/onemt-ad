from django.db import models
import  sqlite3

# Create your models here.
class HistoryInfo8 (models.Model):

    app_key = models.CharField(max_length = 32)
    proctime = models.CharField(max_length= 32)
    datanum = models.CharField(max_length= 32)
    env = models.CharField(max_length= 32)
    nowtime = models.CharField(max_length= 32)
    result = models.CharField(max_length= 32)
class HistoryInfo9 (models.Model):

    app_key = models.CharField(max_length = 32)
    result = models.CharField(max_length= 32)

class HistoryInfo10 (models.Model):

    app_key = models.CharField(max_length = 32)
    result = models.CharField(max_length= 32)

# class User(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=50)
#
#
#     def __unicode__(self):
#         return self.username
class HistoryInfo11 (models.Model):


    result = models.CharField(max_length= 255)