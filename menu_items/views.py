from django.shortcuts import render
from rest_framework import viewsets

from menu_items.serializers import CateogrySerializer, ItemSerializer
from menu_items.models import Category, Item
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the menu index.")

def send_json(request):
    data = {}
    category = Category.objects.all().values()
    items = Item.objects.all().values()

    data['categories'] = list(category)
    data['menu_items'] = list(items)
    return JsonResponse(data)

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CateogrySerializer

class ItemViewSet(viewsets.ModelViewSet):
   queryset = Item.objects.all()
   serializer_class = ItemSerializer