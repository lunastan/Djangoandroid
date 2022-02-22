from django.db import models
class PicPost(models.Model):
    model_pic = models.ImageField(upload_to='image/%Y/%m/%d')
    time = models.DateTimeField(auto_now_add=True)
    userid = models.IntegerField();
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
