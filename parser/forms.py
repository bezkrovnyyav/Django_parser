from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class UserIdForm(forms.Form):
    user_id = forms.IntegerField(
        label='Enter User ID',
        validators=[
            MinValueValidator(1, message='Enter number from 1 to 10'),
            MaxValueValidator(10, message='Enter number from 1 to 10')
        ],
        widget=forms.TextInput(attrs={'autofocus': True})
    )
