from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponForm
from shop.recommender import Recommender


@require_POST
def cart_add(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request.session)
    for item in cart:
        item['update_quantity'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    coupon_form = CouponForm()
    r = Recommender()
    cart_products = [item['product'] for item in cart]
    if cart_products:
        recommended_products = r.suggest_products_for(cart_products, max_results=5)
    else:
        recommended_products = []
    return render(request, 'cart/detail.html',
                  {'cart': cart,
                   'coupon_form': coupon_form,
                   'recommendations': recommended_products})


