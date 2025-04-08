from django.shortcuts import render , HttpResponse , redirect ,  get_object_or_404
from django.utils import timezone
from django.contrib.auth import login , authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from Home import models 
from .models import Carts, Product, Product_Variant
from Cart.models import Carts , CartItems
from .models import Product
from django.contrib.auth import get_user_model

# from models import *

User = get_user_model()

def add_to_cart(request , id):

    product  = Product.objects.get(id = id)
    user = request.user
    cart , _ = Carts.objects.get_or_create(user = user , is_paid= False)
    cart_items   = CartItems.objects.create(cart = cart , product = product )
    
    cart_items.save()
    # try:
    #     cart_items   = CartItems.objects.create(cart = cart , product = product )
    #     # If the product is already in the cart, increase the quantity
    #     cart_items.quantity = quantity+1  # Increase quantity by 1 (You can adjust this as needed)
    #     cart_items.save()
    # except CartItems.DoesNotExist:
    #     # If the product is not in the cart, create a new cart item
    #     cart_items = CartItems.objects.create(cart=cart, product=product, quantity=1)
    
 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def Cart(request ):
    cart = Carts.objects.filter(is_paid=False, user=request.user).first()
    # context = {'cart': cart}
    if cart:
        total_price = cart.Cart_total_price()  # Call instance method on cart instance
        print(total_price)
    else:
        total_price = 0 
    context = {
        'cart': cart,
        'total_price': total_price,
    }
    return render(request, 'Cart/templates/Cart.html', context)






# def cart(request):
#     # User ke cart ko retrieve karen ya naya create karen agar nahi hai
#     cart, created = Carts.objects.get_or_create(user=request.user)

#     # Cart mein maujood saari items ko retrieve karen
#     cart_items = cart.items.all()

#     context = {'cart_items': cart_items}
#     return render(request, 'cart.html', context)

# def add_to_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         product_variant_id = request.POST.get('product_variant_id')
#         quantity = int(request.POST.get('quantity', 1))

#         # User ke cart ko retrieve karen ya naya create karen agar nahi hai
#         cart, created = Carts.objects.get_or_create(user=request.user)

#         # Product aur Product_Variant ko retrieve karen
#         product = Product.objects.get(pk=product_id)
#         product_variant = Product_Variant.objects.get(pk=product_variant_id)

#         # Cart mein item ko add karen
#         cart_item, item_created = Carts.objects.get_or_create(
#             cart=cart,
#             product_id=product,
#             product_variant_id=product_variant
#         )
#         if not item_created:
#             cart_item.quantity += quantity
#             cart_item.save()

#         return redirect('/')
def remove_cart(request , id ):
    try:
        cart_item = CartItems.objects.get(id = id )
        cart_item.delete()
    except Exception as e :
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))