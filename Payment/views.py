from django.shortcuts import render
from Cart.models import Carts
# Create your views here.
# def Delivery(request):
#     return render(request , 'delivery.html')
def payment(request):
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


    
    return render(request , 'payment1.html' , context)
# def ordersuc(request):
#     return render(request , 'order_suc.html')
# def cancle(request):
#     return render(request , 'cancle_suc.html')
# def Reasioncancle(request):
#     return render(request , 'Reasion-cancle.html')