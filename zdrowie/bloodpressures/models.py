from django.db import models
from django.urls import reverse


# Create your models here.
class BloodPressure(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()
    record_datetime = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)


    def get_absolute_url(self):
        return reverse("bloodpressures:detail", kwargs={"pk":self.id})
#
