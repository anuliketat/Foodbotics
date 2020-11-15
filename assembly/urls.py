from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('items/', views.items, name='items'),
    path('add/', views.add_item, name='add_item'),
    path('stations/', views.stations, name='stations'),
    #path('graph/', views.graph, name='graph')
    #path('graph/', name='graph')
]
