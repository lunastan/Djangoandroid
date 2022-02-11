# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='user')
	model_pic = models.ImageField(upload_to='image/%Y/%m/%d')
	lat = models.FloatField(blank=True, null=True)
	lng = models.FloatField(blank=True, null=True)
	time = models.DateTimeField(auto_now_add=True)
