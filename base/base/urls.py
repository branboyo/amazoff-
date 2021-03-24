"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
from pages.views import home_view, produce_view, meat_view, seafood_view, bakery_view, pantry_view, checkout_view
from items.views import item_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('produce/', produce_view),
    path('meat/', meat_view),
    path('pantry/', pantry_view),
    path('seafood/', seafood_view),
    path('bakery/', bakery_view),
    path('item/<int:item_id>/', item_view),
    path('checkout/', checkout_view),
]
