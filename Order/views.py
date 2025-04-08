from django.shortcuts import render

# Create your views here.


def Order(request):
    return render(request , 'Order.html')


def Status(request):
    return render(request , 'status.html')