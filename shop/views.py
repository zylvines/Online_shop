from django.shortcuts import render
from django.shortcuts import render
from .models import Product


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def detail(request):
    return render(request, 'shop/detail.html')

def product_list(request):
    filter_by = request.GET.get("filter_by", None)
    products = Product.objects.all()

    if filter_by == "expensive":
        products = products.order_by("-original_price")
    elif filter_by == "cheap":
        products = products.order_by("original_price")
    elif filter_by == "likes":
        products = products.order_by("-likes")

    return render(request, "product_list.html", {"products": products})
