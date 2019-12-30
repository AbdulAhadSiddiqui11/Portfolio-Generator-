from django.db import models
from django.contrib.auth.models import User


# TODO: Check the date function -> Add present date function

class UserInfo(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    headline = models.CharField(max_length = 250)
    about = models.TextField()
    github = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='user_profiles')
    user = models.ForeignKey(User, on_delete = models.CASCADE)


class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    startdate = models.DateField()
    endate = models.DateField()
    desc = models.TextField(blank=True)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)

class School(models.Model):
    school = models.CharField(max_length=100)
    startdate = models.DateField()
    endate = models.DateField()
    desc = models.TextField(blank=True)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    issuedate = models.DateField()
    expiration = models.DateField()
    cred_id = models.CharField(max_length=100)
    cred_url = models.CharField(max_length=150)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)

class Volunteering (models.Model):
    org = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    startdate = models.DateField()
    endate = models.DateField()
    desc = models.TextField(blank=True)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)

class Skill(models.Model):
    name = models.CharField(max_length=40)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    startdate = models.DateField()
    endate = models.DateField()
    link = models.CharField(max_length=150)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)

class Award(models.Model):
    name = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    date = models.DateField()
    desc = models.TextField(blank=True)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    startdate = models.DateField()
    endate = models.DateField()
    desc = models.TextField(blank=True)
    userinfo = models.ForeignKey(UserInfo, on_delete = models.CASCADE)


