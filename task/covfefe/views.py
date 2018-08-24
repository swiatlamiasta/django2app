from django.shortcuts import render

def index(request, template_name='covfefe/index.html'):
    return render(request, template_name, {})

def providers(request, template_name='covfefe/providers.html'):
    return render(request, template_name, {})

def offers(request, template_name='covfefe/offers.html'):
    return render(request, template_name, {})
