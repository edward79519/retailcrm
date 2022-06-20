from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from core.models import Company

# Create your models here.


class CallType(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CallRecord(models.Model):
    sn = models.CharField(max_length=9)
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='callrecords',
    )
    calldate = models.DateField()
    calltype = models.ForeignKey(
        CallType,
        on_delete=models.PROTECT,
        related_name='callrecords',
    )
    questions = models.CharField(max_length=1000)
    requirement = models.CharField(max_length=1000)
    attachment = models.FileField(
        upload_to='callrecord/%Y/%m/',
        blank=True,
        null=True,
    )
    summary = models.CharField(max_length=200)
    nextdate = models.DateField()
    auther = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='callrecords',
    )
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return "{}_{}".format(self.calldate, self.company)


class Participants(models.Model):
    record = models.ForeignKey(
        CallRecord,
        on_delete=models.CASCADE,
        related_name='participants',
    )
    side = models.BooleanField(default=True)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name
