# tours/forms.py
from django import forms
from .models import Tour, Guide, Review, TourGuide, Tourist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class TourForm(forms.ModelForm):
#     class Meta:
#         model = Tour
#         fields = ['name_tour', 'date_of_start', 'date_of_end', 'description', 'price']

class TourForm(forms.ModelForm):
    guides = forms.ModelMultipleChoiceField(
        queryset=Guide.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Tour
        fields = ['name_tour', 'date_of_start', 'date_of_end', 'description', 'price']

    def save(self, commit=True):
        tour = super().save(commit=False)
        if commit:
            tour.save()
        tour.tourguide_set.all().delete()  # Удаляем все существующие связи
        for guide in self.cleaned_data['guides']:
            TourGuide.objects.create(tour=tour, guide=guide)
        return tour


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            Tourist.objects.get_or_create(user=user, defaults={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': self.cleaned_data['phone']
            })
        return user

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ['first_name', 'last_name', 'language', 'email', 'phone']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and not (1 <= rating <= 5):
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating

class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth']
    
    def __init__(self, *args, **kwargs):
        super(TouristForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control', 'type': 'date'})


class GuideSearchForm(forms.Form):
    last_name = forms.CharField(label='Last Name', max_length=30, required=False)


class TourSearchForm(forms.Form):
    name_tour = forms.CharField(label='Tour Name', max_length=100, required=False)
