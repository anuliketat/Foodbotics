from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Item
from . serializers import ItemSerializer

from . models import Item, Prep_methods, ItemProfile
from . forms import AddNewItem, ItemFormset
import re

# Create your views here.
"""
class ItemsList(APIView):
    def get(self, request):
        Items = Item.objects.all()
        serializer = ItemSerializer(Items, many=True)

        return Response(serializer.data)

def graph(response):
    json = {'id':id,
            'primaryI':chicken_marinate,
            'primaryT':grilling,
            'primaryTime':5,
            'secondaryI':[ingredients, seasonings],
            'secondaryT':stewing,
            'secondaryTime':15}
    return render(response, 'assembly/graph.html')
"""
def items(response):
    obj = Item.objects.all().order_by("name")
    context = {'name':obj}
    #stations = ItemProfile.
    return render(response, 'assembly/items.html', context)

def admin(response):
    obj = Item.objects.all()
    context = {'name':obj}
    return render(response, 'assembly/admin.html', context)

def add_item(response):
    if response.method == 'GET':
        form = AddNewItem(response.GET or None)
        form_set = ItemFormset(response.GET or None)
    elif response.method == "POST":
        form = AddNewItem(response.POST)
        form_set = ItemFormset(response.POST)
        if form.is_valid():
            n = form.cleaned_data["item"]
            c = form.cleaned_data["cuisine"]
            i = Item(name=n, cuisine=c)
            i.save()
        if form_set.is_valid():
            for form in form_set:
                print(form.cleaned_data)
                task = form.cleaned_data.get('source_station', None)
                if task is not None:
                    #ItemProfile(stations=name).save()
                    print(task)
    else:
        form = AddNewItem()
    #if response.POST.get('save') == 'save':
        #formset = AddItemTasks(response.POST)

    context = {'form':form, 'formset':form_set}
    return render(response, 'assembly/add.html', context)

def stations(response):
    obj = Prep_methods.objects.all().order_by("method")
    dic = {}
    for i in range(len(obj)):
        dic[obj[i]] = obj[i].types
    for i in dic.keys():
        dic[i] = re.split(', ', dic[i])
        dic[i] = [j.capitalize() for j in dic[i]]

    context = {'name':dic}
    return render(response, 'assembly/stations.html', context)



