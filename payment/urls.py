from . import views, webhooks
from django.urls import path

app_name = 'payment'


urlpatterns = [
    path('/process', views.payment_process, name='process'),
    path('/completed', views.payment_complete, name='completed'),
    path('/canceled', views.payment_canceled, name='canceled'),
    path('/webhook', webhooks.stripe_webhook, name='stripe-webhook')
]