from django import forms
from .models import Provider, Offer

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['user','provider_name']