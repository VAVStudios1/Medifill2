from django.db import models
from Home.models import CustomUser
from Order.models import Orders

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , null = True)  # Assuming User is the built-in Django User model
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)  # Assuming you have an Order model
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
