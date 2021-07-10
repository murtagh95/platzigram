""" User Forms. """

# Django
from django import forms

class ProfileForm(forms.Form):
    website = forms.URLField(
        label='Website',
        required=True,
        max_length=200
    )
    biography = forms.CharField(
        label='biography',
        max_length=500,
        required=False
    )
    phone_number = forms.CharField(
        label='Phone number',
        max_length=20,
        required=False
    )
    picture = forms.ImageField()