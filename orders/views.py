from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderForm
from cart.cart import Cart
from .tasks import order_created
from loguru import logger


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            logger.info(Order.objects.all())
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
