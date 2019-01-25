from django.contrib import admin
from .models import Schooldetails
# Register your models here.
@admin.register(Schooldetails)
class SchooldetailsAdmin(admin.ModelAdmin):
    list_display = ('name','level')
