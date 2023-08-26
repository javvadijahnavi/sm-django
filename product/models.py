from django.db import models


# Create your models here.
class Product(models.Model):
    product_code = models.CharField(max_length=8)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "%s -- %s" % (self.product_code, self.name)


class Discount(models.Model):
    discount_code = models.CharField(max_length=8)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "%s -- %s" % (self.discount_code, self.discount_price)


class Cart(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    discount = models.ForeignKey(to=Discount, on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return "%s" % self.product


class CheckOut(models.Model):
    products_in_cart = models.JSONField()

    def __str__(self):
        return "%s -- %s" % (self.products_in_cart, self.final_price)