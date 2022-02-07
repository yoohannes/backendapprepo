from tkinter import CASCADE
from django.db import models


class Tester(models.Model):
    tester_ID = models.BigAutoField(primary_key=True)
    test_id = models.IntegerField()
    time = models.CharField(max_length=200)
    phone_manufacturer = models.CharField(max_length=200)
    phone_model = models.CharField(max_length=200)
    screen_height = models.CharField(max_length=200)
    screen_width = models.CharField(max_length=200)

    def __str__(self):

        return self.phone_model


class Video(models.Model):
    duration = models.IntegerField()
    time = models.BigIntegerField()
    video_file = models.FileField(null=False, blank=False, default="testdef")
    tester = models.OneToOneField(
        Tester, on_delete=models.CASCADE, blank=True, null=True
    )


class Pics(models.Model):

    height = models.IntegerField()
    time = models.BigIntegerField()
    width = models.IntegerField()
    pic_num = models.IntegerField()
    image = models.TextField()
    tester = models.ForeignKey(
        Tester, on_delete=models.CASCADE, to_field="tester_ID", blank=True, null=True
    )
