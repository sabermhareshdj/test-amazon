from rest_framework import serializers                       
from .models import Cart,CartDetail,Order,OrderDetail
from product.serializers import ProductListSerializer

class CartDetailSerializer(serializers.ModelSerializer):
    #product = ProductListSerializer()
    product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_Detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'