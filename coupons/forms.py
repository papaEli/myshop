from django import forms
from .models import Coupon


class CouponForm(forms.Form):
    code = forms.CharField()

