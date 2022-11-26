from django.db import models
from django.urls import reverse


# Create your models here.
class Glucose(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()
    record_datetime = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("glucoses:detail", args=[self.id])
