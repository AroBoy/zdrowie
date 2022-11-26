from django.contrib import admin
from .models import Glucose

# Register your models here.
@admin.register(Glucose)
class GlucoseAdmin(admin.ModelAdmin):
    list_display = ['user', 'value', 'record_datetime']
