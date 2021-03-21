from django.shortcuts import render

from .models import Item
# Create your views here.
def item_view(request, item_id):
    obj = Item.objects.get(id = item_id)
    context = {
        'item':obj,
    }
    return render(request, "details.html", context)