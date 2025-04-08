from django.db import models

# Create your models here.
class Product_Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.category_name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    url_slug = models.SlugField(null=True)
    cat_id = models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    product_image = models.ImageField(null=True , blank=True)
    description = models.TextField()
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    prescription = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')]  , default='No')

    def __str__(self):
        return self.product_name
    
    @staticmethod
    def total_price_of_products():
        total_price = Product.objects.aggregate(total=models.Sum('price'))['total']
        return total_price

    @property
    def imageURL(self):
        try:
            url=self.product_image.url
        except:
            url=''
        return url

class Product_Variant(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_medi_mg = models.CharField(max_length=20)
    medi_quantity = models.PositiveSmallIntegerField()
    price = models.FloatField()
    stock_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product_id.product_name} - {self.size_medi_mg} - {self.medi_quantity}"
    

    