from datetime import timezone
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import CouponForm
from .models import Coupon
from django.views.decorators.http import require_POST
from django.contrib import messages
from loguru import logger


@require_POST
def coupon_apply(request):
    now = timezone.now()
    code = request.POST.get('code')
    try:
        coupon = Coupon.objects.get(code__iexact=code,
                                    active=True)
        request.session["coupon_id"] = coupon.id
        logger.debug(
            f"COUPON APPLY SUCCESS: Applied coupon {coupon.id}")
    except Coupon.DoesNotExist:
        logger.warning(f"Код купона {code} не найден. Параметры поиска: "
                       f"valid_from lte={now}, valid_to gte={now}, active=True")
        messages.error(request, f'Coupon {code} does not exist')

    return redirect('cart:cart_detail')
