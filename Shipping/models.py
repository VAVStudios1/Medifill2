from django.db import models
from Order.models import Orders

# Create your models here.
class Shipping_addresses(models.Model):
    id = models.AutoField(primary_key=True )
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    full_address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return f"Shipping Address for {self.full_address}"