from django.shortcuts import render

def index(request, template_name='covfefe/index.html'):
    return render(request, template_name, {'test': test})
