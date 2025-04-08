from django.db import models
from Home.models import CustomUser
# from django.utils import timezone
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)
    


class ShopOwner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=255 ,null = True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , null = True)
    phone_number = models.BigIntegerField(null=True)
    full_address = models.CharField(max_length=255, blank=True , null=True)
    state = models.CharField(max_length=100 , blank=True , null=True)
    city = models.CharField(max_length=100 , blank=True , null=True)
    pin_code = models.CharField(max_length=20 , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.user.name
# class ShopOwner(AbstractBaseUser, PermissionsMixin):
#     owner_id = models.AutoField(primary_key=True)
#     email = models.EmailField(unique=True)
#     ShopOwner_image = models.ImageField(null= True)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_number = models.BigIntegerField()
#     full_address = models.CharField(max_length=255)
#     state = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     pin_code = models.CharField(max_length=20)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255) 
    license_expiry_date = models.DateTimeField()
    full_address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=20)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
       return self.shop_name
