from django.shortcuts import render, get_object_or_404
from .models import Bikes, Product, Company
from .filter import ProductFilter




# Create your views here.
def all_products(request):
    products = Product.products.all()[:6]
    # products = Product.objects.filter(in_stock=True)  # in_stock set to true will filter products which are out of stock
    return render(request, 'store/home.html', {'products': products})



def total_products(request):
    products = Product.products.all()
    brand = request.GET.get('brand')
    if brand:
        # products = ProductFilter(request.GET, queryset=products).qs
        products = Product.products.filter(part_name=brand)
    # filtered = ProductFilter(request.GET, queryset=products)
    return render(request, 'store/products/products.html', {'products': products})


"""def product_detail(request, part_name):
    product = get_object_or_404(Product, part_name=part_name)
    return render(request, 'store/products/details.html', {'product': product})
"""


def detail_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/products/details.html', {'product': product})


def bikes_list(request, bike_slug):
    bikes = get_object_or_404(Bikes, slug=bike_slug)
    products = Product.objects.filter(bikes=bikes)
    return render(request, 'store/products/bikes.html', {'bikes': bikes, 'products': products})

