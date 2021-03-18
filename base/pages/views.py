from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args, **kwargs):
    return render(request, "home.html", {})

def electronics_view(request,*args, **kwargs):
    context = {
        "Category": "Electronics",
        "Title": "Amazoff: Electronics Catalog"
    }
    return render(request, 'category.html', context)