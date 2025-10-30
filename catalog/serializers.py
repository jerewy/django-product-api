from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail")
    
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'description', 'price', 'created_at']