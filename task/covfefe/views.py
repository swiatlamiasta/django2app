from django.shortcuts import render
from .models import Provider, Offer

def index(request, template_name='covfefe/index.html'):
    return render(request, template_name, {})

def providers(request, template_name='covfefe/providers.html'):
    providers = Provider.objects.all()
    return render(request, template_name, {'providers': providers})

def offers(request, template_name='covfefe/offers.html'):
    offers = Offer.objects.all()
    return render(request, template_name, {'offers': offers})
