from django import forms
from .models import Provider, Offer

class ProviderForm(forms.ModelForm):
    user=1
    class Meta:
        model = Provider
        fields = ['provider_name']