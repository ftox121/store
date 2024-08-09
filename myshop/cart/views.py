from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProduct
from shop.models import Product


# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProduct(require_POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity = cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')