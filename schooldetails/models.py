from django.db import models

# Create your models here.
class Schooldetails(models.Model):
    logo = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tag1 = models.CharField(max_length=255, blank=True, null=True)
    tag2 = models.CharField(max_length=255, blank=True, null=True)
    tag3 = models.CharField(max_length=255, blank=True, null=True)
    tag4 = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    weburl = models.CharField(max_length=255, blank=True, null=True)
    introduce = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schooldetails'


class Schoolscore(models.Model):
    schoolname = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    pici = models.CharField(max_length=255, blank=True, null=True)
    ambit = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    average = models.CharField(max_length=255, blank=True, null=True)
    maxscore = models.CharField(max_length=255, blank=True, null=True)
    minscore = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schoolscore'


class Specialtydetails(models.Model):
    schoolname = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    introduce = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialtydetails'


class Specialtyscore(models.Model):
    schoolname = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    ambit = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    specialtyname = models.CharField(max_length=255, blank=True, null=True)
    average = models.CharField(max_length=255, blank=True, null=True)
    maxscore = models.CharField(max_length=255, blank=True, null=True)
    minscore = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialtyscore'
