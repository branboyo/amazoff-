from django.shortcuts import render
from django.http import HttpResponse
from items.models import Item

# Create your views here.

def home_view(request,*args, **kwargs):
    context = {
        "item1": Item.objects.get(id = 1)
    }
    return render(request, "home.html", context)

def electronics_view(request,*args, **kwargs):
    context = {
        "Category": "Electronics",
        "Title": "Amazoff: Electronics Catalog"
    }
    return render(request, 'category.html', context)

def groceries_view(request,*args, **kwargs):
    context = {
        "Category": "Groceries",
        "Title": "Amazoff: Groceries Catalog"
    }
    return render(request, 'category.html', context)

def furnitures_view(request,*args, **kwargs):
    context = {
        "Category": "Furnitures",
        "Title": "Amazoff: Furnitures Catalog"
    }
    return render(request, 'category.html', context)

def cleaning_products_view(request,*args, **kwargs):
    context = {
        "Category": "Cleaning Products",
        "Title": "Amazoff: Cleaning Products Catalog"
    }
    return render(request, 'category.html', context)

def office_supplies_view(request,*args, **kwargs):
    context = {
        "Category": "Office Supplies",
        "Title": "Amazoff:  Office Supplies Catalog"
    }
    return render(request, 'category.html', context)