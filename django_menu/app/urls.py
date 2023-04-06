from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deals.html', views.deals, name='deals'),
    path('about.html', views.about, name='about'),
    path('sale.html', views.sale, name='sale'),
    path('free.html', views.free, name='free'),
    path('freee.html', views.freee, name='freee'),
]
