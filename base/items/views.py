from django.shortcuts import render, get_object_or_404

from .models import Item
# Create your views here.
def item_view(request, item_id):
    obj = get_object_or_404(Item, id=item_id)
    context = {
        'item':obj,
    }
    return render(request, "details.html", context)