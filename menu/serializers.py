from rest_framework import serializers, status
from .models import MenuCategory, MenuProducts, MenuOrder


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']



class MenuProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuProducts
        fields = ['id', 'name', 'price', 'description', 'image', 'category']


class MenuOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOrder
        fields = ['id','product', 'quantity', 'order_date', 'location', 'payment_method']
