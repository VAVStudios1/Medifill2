from django.contrib import admin
from Product.models import Product_Category , Product , Product_Variant

# Register your models here.

admin.site.register(Product_Category)
admin.site.register(Product)
admin.site.register(Product_Variant)