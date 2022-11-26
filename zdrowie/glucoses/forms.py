from django import forms
from .models import Glucose

class GlucoseForm(forms.ModelForm):
    record_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type':'datetime-local', 'class': 'form-control'})
    )
    class Meta:
        model = Glucose
        exclude = ["user"]
