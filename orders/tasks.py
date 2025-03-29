from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from myshop import settings


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)

    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n'
    message += f'Your order has been created.'
    message += f'\nYour order id is {order.id}'

    mail_sent = send_mail(
        subject, message,
        settings.EMAIL_HOST_USER,
        [order.email]
    )
    return mail_sent
