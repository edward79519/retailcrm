import datetime
import os

from django import template

register = template.Library()


@register.filter
def filename(value):
    return os.path.basename(value.file.name)


@register.filter
def datedelta(value):
    if value:
        deltaday = (datetime.date.today() - value).days
        if deltaday == 0:
            dt = "今天"
        elif deltaday == 1:
            dt = "昨天"
        elif deltaday < 7:
            dt = "{}天前".format(deltaday)
        elif deltaday < 30:
            dt = "{}個星期前".format(deltaday // 7)
        elif deltaday < 365:
            dt = "{}月前".format(deltaday // 30)
        else:
            dt = "{}年前".format(deltaday // 365)
    else:
        dt = "尚未拜訪"
    return dt


@register.filter
def firstparti(record):
    first_parti = record.participants.filter(side=True).first()
    if first_parti:
        return "{}-{}".format(first_parti.name, first_parti.title)
    else:
        return ""


@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })
