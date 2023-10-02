from rest_framework.serializers import serializers                       
from .models import Cart,CartDetail,Order,OrderDetail

class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    CartDetail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'
