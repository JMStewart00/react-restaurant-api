from rest_framework import serializers

from menu_items.models import Category, Item

class CateogrySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ['title']


class ItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = Item
       fields = '__all__'