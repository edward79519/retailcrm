from django.contrib import admin
from .models import CallType, CallRecord, Participants

# Register your models here.
admin.site.register(CallType)
admin.site.register(CallRecord)
admin.site.register(Participants)
