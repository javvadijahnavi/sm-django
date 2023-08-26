from django.contrib import admin
from .models import Cart, Product, Discount, CheckOut

# Register your models here.
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(CheckOut)
