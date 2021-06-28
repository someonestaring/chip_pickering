from django import forms
from app_chip.models import *

class VisitorForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, max_length=56)
    email = forms.EmailField(
        label='Email Address',
        max_length=120,
        required=True,
        widget=forms.EmailInput)
    description = forms.CharField(widget=forms.Textarea, max_length=256)