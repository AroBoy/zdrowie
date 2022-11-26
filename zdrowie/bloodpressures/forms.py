from django import forms
from .models import BloodPressure


class BloodpressureForm(forms.ModelForm):
    record_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )

    class Meta:
        model = BloodPressure
        exclude = ["user"]
