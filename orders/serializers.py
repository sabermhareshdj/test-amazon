from rest_framework import serializers                       
from .models import Cart,CartDetail,Order,OrderDetail
from product.serializers import ProductListSerializer

class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    #product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    coupon = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = '__all__'


class OrderListserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    model = OrderDetail
    fields = '__all__'



class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    products = OrderProductSerializer(many=True,source='order_detail')
    class Meta:
        model = Order
        fields = '__all__'

