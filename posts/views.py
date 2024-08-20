from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.http import HttpResponseNotFound

def index(request):
    return render(request, 'index.html')

def dynamic_page(request, page):
    template_name = f'{page}.html'
    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        return HttpResponseNotFound(f'Page {page} not found.')


# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

# def category(request):
#     return render(request, 'category.html')

# def contact(request):
#     return render(request, 'contact.html')

# def singlepost(request):
#     return render(request, 'singlepost.html')

# def starterpage(request):
#     return render(request, 'starterpage.html')