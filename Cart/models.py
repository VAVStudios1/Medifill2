from django.db import models
from Product.models import Product , Product_Variant
from Home.models import CustomUser
# Create your models here.
class Carts(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , null = True)
    is_paid = models.BooleanField(default=False)

    def Cart_total_price(self):
        cart_items = self.cart_items.all()
        price = []
        for cart_item in cart_items:
            price.append(cart_item.product.price)
        return sum(price)


class CartItems(models.Model):
    cart = models.ForeignKey(Carts ,  on_delete=models.CASCADE , related_name='cart_items')
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True , blank=True)
    product_variant  = models.ForeignKey(Product_Variant , on_delete=models.SET_NULL , null=True , blank=True)
    quantity = models.PositiveIntegerField(default=1)


    