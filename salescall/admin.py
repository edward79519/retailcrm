from django.contrib import admin
from .models import CallType, CallRecord, Participants, Comment

# Register your models here.


class ParticipantsInlineAdmin(admin.TabularInline):
    model = Participants


class CallRecordAdmin(admin.ModelAdmin):
    inlines = [ParticipantsInlineAdmin]


admin.site.register(Participants)
admin.site.register(CallType)
admin.site.register(Comment)
admin.site.register(CallRecord, CallRecordAdmin)
