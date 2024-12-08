# tours/forms.py
from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name_tour', 'date_of_start', 'date_of_end', 'description', 'price']
