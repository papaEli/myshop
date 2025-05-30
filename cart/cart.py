from decimal import Decimal
from django.conf import settings
from shop.models import Product
from coupons.models import Coupon
from loguru import logger

logger.info('Логирование корзины начато')


class Cart:

    def __init__(self, session):
        self.session = session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')
        logger.debug(f"Купон {self.coupon_id}")

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
            return None

    def get_discount(self):
        logger.debug("Метод get_discount вызван!")
        if self.coupon:
            logger.debug('Купон найден!')
            discount_amount = (Decimal(self.coupon.discount) / Decimal(100)) * self.get_total_price()
            logger.debug(f"Исходная стоимость: {self.get_total_price()}")
            logger.debug(f'Скидка: {discount_amount}')
            return discount_amount.quantize(Decimal('.01'))
        logger.warning('Купон не найден..')
        return Decimal('0.00')

    def get_total_price_after_discount(self):
        total = self.get_total_price()
        discount = self.get_discount()
        logger.debug(f'Итоговая стоимость {total - discount}')
        return (total - discount).quantize(Decimal('.01'))
