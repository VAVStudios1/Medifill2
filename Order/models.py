from django.db import models
from Product.models import Product  , Product_Variant

# Create your models here.


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(unique=True, max_length=50)
    # user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total_amount = models.FloatField(default=1500)
    discount_amount = models.FloatField(default=100)
    gross_amount = models.FloatField(default=1400)
    shipping_amount = models.FloatField(default=50)
    net_amount = models.FloatField(default=1450)
    STATUS_CHOICES = [
        ('placed', 'Placed'),
        ('processing', 'Processing'),
        ('shipping', 'Shipping'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('not_paid', 'Not Paid'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    PAYMENT_TYPE_CHOICES = [
        ('net_banking', 'Net Banking'),
        ('upi', 'UPI'),
        ('cash_on_delivery', 'Cash on Delivery'),
    ]
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    payment_transaction_id = models.CharField(unique=True, max_length=100)

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variant_id = models.ForeignKey(Product_Variant, on_delete=models.CASCADE)
    # product_name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total_amount = models.FloatField()

    def __str__(self):
        return self.product_id.product_name


# class OrderShippingAddresses(models.Model):
#     id = models.AutoField(primary_key=True)
#     shipping_address_id = models.ForeignKey(Shipping_addresses, on_delete=models.CASCADE )
#     order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    
#     full_address = models.TextField()
#     state = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     pin_code = models.CharField(max_length=10)

#     def __str__(self):
#         return self.id


