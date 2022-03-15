from rest_framework import serializers

from menu_items.models import Category, Item, Cuisine

class CateogrySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ['title']

class CuisineSerializer(serializers.ModelSerializer):
   class Meta:
       model = Cuisine
       fields = ['label']


class ItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = Item
       fields = '__all__'