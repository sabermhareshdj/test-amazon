from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand , ProductImages , Review
from django.db.models import Q , F , Value
#from django.db.models.aggregates import max,Min,Count,Avg,Sum
from django.db.models.aggregates import Count



# Create your views here.
def queryset_debug(request):
    # data = Product.objects.select_related('brand').all() #prefetch_related = many-to-many
    #data = Product.objects.filter(price__gt =70) #اكبر من 70
    #data = Product.objects.filter(price__gte = 70) اكبر من او يساوي
    #data = Product.objects.filter(price__lt =70) # اقل من
    #data = Product.objects.filter(price__lte =70) # اقل من او يساوي
    #data = Product.objects.filter(price__range = (60,70))

    # navigate relation
    #data = Product.objects.filter(brand__name='pro')
    #data = Product.objects.filter(brand__name__gt = 20)

    # filter with text 
    #data = Product.objects.filter(name__contains = 'Brown')
    #data = Product.objects.filter(name__startwith = 'Brown')
    data = Product.objects.filter(name__endswith = 'e')
    #data = Product.objects.filter(tags__isnull = True)

    # filter date time
    #data = Review.objects.filter(created_at__year = 2023)

    #data = Product.objects.filter(price__gt=80 , quantity__lt =10 ) # and
    #data = Product.objects.filter(
      #  Q(price__gt=80) |
     #   Q(quantity__lt =10)
    # ) # or #from django.db.models import Q
    
    #data = Product.objects.filter(
    #    Q(price__gt=80) & 
    #    Q(quantity__lt =10)
    #   ) # and  #from django.db.models import Q
    
    #data = Product.objects.filter(
    #    Q(price__gt=80) & 
    #    ~Q(quantity__lt =10)  # اكبر و ليس اصغؤ ّ
    #   ) # and  #from django.db.models import Q  # or with not
 #   data = Product.objects.filter(price=F('quantity')) # F filed #from django.db.models import Q , F

    return render(request,'product/debug.html', {'data':data})

class ProductList(ListView):
    model = Product         # context : object_list , model_list
    paginate_by = 30


class ProductDetail(DetailView):
    model = Product          # context : object   : model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    

class BrandList(ListView):
    model = Brand       # context : object_list , model_list
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    paginate_by = 20
    


class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    paginate_by = 20   

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context