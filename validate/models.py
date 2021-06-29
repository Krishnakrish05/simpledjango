from django.db import models

# Create your models here.


class Request(models.Model):
    reqid = models.AutoField(db_column='req_id', primary_key=True)
    firstname = models.CharField(max_length=25, null=False)
    lastname = models.CharField(max_length=25, null=False)
    dob = models.CharField(null=False, max_length=15)
    gender = models.CharField(max_length=10, null=False)
    nationality = models.CharField(max_length=10, null=False)
    state = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    pincode = models.CharField(max_length=10, null=False)
    qualification = models.CharField(max_length=10, null=False)
    salary = models.IntegerField(null=False)
    pannumber = models.CharField(null=False, max_length=12)
