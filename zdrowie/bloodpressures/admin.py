from django.contrib import admin
from .models import BloodPressure

# Register your models here.
@admin.register(BloodPressure)
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ['user', 'systolic', 'diastolic', 'pulse', 'record_datetime']
