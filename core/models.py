from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


# Category of industry defined by taiwan government
class Category(models.Model):
    sn = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return "{}.{}".format(self.sn, self.name)


# Where the Customer coming from
class Source(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


# Rank of the customer
class Rank(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name


# Asking status of customer
class Status(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField()

    def __str__(self):
        return self.name


# County of Address
class County(models.Model):
    sn = models.CharField(max_length=2)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# Customer detail
class Company(models.Model):
    fullname = models.CharField(max_length=100, unique=True)
    shortname = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="company",
        blank=True,
        null=True,
    )
    rank = models.ForeignKey(
        Rank,
        on_delete=models.PROTECT,
        related_name="company",
        blank=True,
        null=True,
    )
    sn = models.CharField(
        max_length=9,
        unique=True,
    )
    stock_id = models.CharField(
        max_length=6,
        unique=True,
        blank=True,
        null=True,
    )
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="company",
        blank=True,
        null=True,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="company",
        blank=True,
        null=True,
    )
    addr_county = models.ForeignKey(
        County,
        on_delete=models.PROTECT,
        related_name="company",
        blank=True,
        null=True,
    )
    addr_detail = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    contact_tel = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    report = models.FileField(
        upload_to="company/%Y/%m/",
        blank=True,
        null=True,
    )
    pwr_usage = models.DecimalField(max_digits=11, decimal_places=1, blank=True, null=True)
    pwr_inquire = models.DecimalField(max_digits=11, decimal_places=1, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    duration = models.IntegerField(default=0)
    warn_date = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    sponsor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="compspnsr",
    )
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="compauth",
    )
    is_draft = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return "{}-{}".format(self.sn, self.shortname)
