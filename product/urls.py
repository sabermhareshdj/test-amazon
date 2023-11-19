from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail , queryset_debug ,add_review
from .api import ProductDetailAPI,ProductListAPI,BrandDetailAPI,BrandListAPI
from orders.api import ApplyCouponAPI

app_name = 'product'


urlpatterns = [
    path('' , ProductList.as_view()),
    path('debug' ,queryset_debug ),
    path('<slug:slug>' , ProductDetail.as_view()),
    path('<slug:slug>/add-review' , add_review,name='add-review'),

    path('brands/' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),

    #api
    path('api/list' , ProductListAPI.as_view()),
    path('api/list/<int:pk>' , ProductDetailAPI.as_view()),
    path('brands/api/list' , BrandListAPI.as_view()),
    path('brands/api/list/<int:pk>' , BrandDetailAPI.as_view()),
    path('api/<str:username>/cart/apply-coupon' , ApplyCouponAPI.as_view()),


]