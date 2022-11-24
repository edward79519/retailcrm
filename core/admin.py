from django.contrib import admin
from .models import Category, Source, Rank, Status, County, Company


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')


# Register your models here.
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Rank)
admin.site.register(Status, StatusAdmin)
admin.site.register(County)
admin.site.register(Company)
