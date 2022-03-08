from itertools import product
from django.forms import SlugField
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from store.models import Cart, Order, Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})

def detail_product(request, slug):
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'store/detail.html',context={"product":product} )

def aad_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug = slug)
    cart, _ = Cart.objects.get_or_create(user = user)
    order,created = Order.objects.get_or_create(user= user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        cart.quantity += 1
        order.save( )

    
