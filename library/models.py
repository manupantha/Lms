from django.db import models


# Create your models here.
class Member(models.Model):
    member_name = models.CharField(max_length=100)
    member_name = models.CharField(max_length=100)


class Magazine(models.Model):
    magazine_name = models.CharField(max_length=100)
