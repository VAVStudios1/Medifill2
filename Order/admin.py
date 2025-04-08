from django.contrib import admin
from Order.models import Orders , OrderItems 

# Register your models here.

admin.site.register(Orders)
admin.site.register(OrderItems)
# admin.site.register(OrderShippingAddresses)
