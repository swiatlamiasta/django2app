from django.shortcuts import render, redirect
from .models import Provider, Offer
from .forms import ProviderForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request, template_name='covfefe/index.html', name='index'):
    return render(request, template_name, {})

@login_required
def providers(request, template_name='covfefe/providers.html', name='providers'):
    providers = Provider.objects.all()
    return render(request, template_name, {'providers': providers})

@login_required
def offers(request, template_name='covfefe/offers.html', name='offers'):
    offers = Offer.objects.all()
    return render(request, template_name, {'offers': offers})

@login_required
def add_provider(request, template_name='covfefe/add_provider.html', name='add_provider'):
    form = ProviderForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('providers')    
    return render(request, template_name, {'form': form})
