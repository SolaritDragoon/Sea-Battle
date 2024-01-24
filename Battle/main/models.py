from django.db import models



class account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20, blank=False, null=False)


class priz(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    category = models.CharField(max_length=20, blank=False, null=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')