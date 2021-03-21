from django.shortcuts import render
from django.http import HttpResponse
from items.models import Item

# Create your views here.

def home_view(request,*args, **kwargs):
    context = {
        "item1": Item.objects.get(id=1),
        "item2": Item.objects.get(id=2),
        "item3": Item.objects.get(id=3),
        "item4": Item.objects.get(id=4),
        "item5": Item.objects.get(id=5),
        "item6": Item.objects.get(id=6),
        "item7": Item.objects.get(id=7),
        "item8": Item.objects.get(id=8),
        "item9": Item.objects.get(id=9),
        "item10": Item.objects.get(id=10),
        "item11": Item.objects.get(id=11),
        "item12": Item.objects.get(id=12),
        "item13": Item.objects.get(id=13),
        "item14": Item.objects.get(id=14),
        "item15": Item.objects.get(id=15),
        "item16": Item.objects.get(id=16),
        "item17": Item.objects.get(id=1),
        "item18": Item.objects.get(id=1),
        "item19": Item.objects.get(id=1),
        "item20": Item.objects.get(id=1),
        "item21": Item.objects.get(id=1),
        "item22": Item.objects.get(id=1),
        "item23": Item.objects.get(id=1),
        "item24": Item.objects.get(id=1),
        "item25": Item.objects.get(id=1),
        "item26": Item.objects.get(id=1),
        "item27": Item.objects.get(id=1),
        "item28": Item.objects.get(id=1),
        "item29": Item.objects.get(id=1),
        "item30": Item.objects.get(id=1),
        "item31": Item.objects.get(id=1),
        "item32": Item.objects.get(id=1),
        "item33": Item.objects.get(id=1),
        "item34": Item.objects.get(id=1),
        "item35": Item.objects.get(id=1),
        "item36": Item.objects.get(id=1)
    }
    return render(request, "home.html", context)

def electronics_view(request,*args, **kwargs):
    itemlist = Item.objects.filter(description = "produce")
    context = {
        "Category": "Electronics",
        "Title": "Amazoff: Electronics Catalog",
        "list": itemlist,
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