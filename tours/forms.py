# tours/forms.py
from django import forms
from .models import Tour, Guide, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name_tour', 'date_of_start', 'date_of_end', 'description', 'price']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ['first_name', 'last_name', 'language', 'email', 'phone']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']