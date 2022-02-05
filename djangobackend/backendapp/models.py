
from django.db import models

# Create your models here.
class Tester(models.Model):
    tester_ID=models.BigAutoField(primary_key=True)
    test_id=models.IntegerField()
    time=models.CharField(max_length=200)
    phone_manufacturer=models.CharField(max_length=200)
    phone_model=models.CharField(max_length=200)
    screen_height=models.CharField(max_length=200)
    screen_width=models.CharField(max_length=200)
    video_file=models.FileField(null=False,blank=False,default="testdef")
    def __str__(self):
        return self.phone_model
