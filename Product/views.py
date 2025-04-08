from django.shortcuts import render
from Product.models import Product

# Create your views here.

def Product_view(request , product_name):
    product = Product.objects.get(product_name=product_name)
    context = {'product': product}


    return render(request , 'Product/templates/Product_view.html' , context)




def Product_search(request):
    query = request.GET.get('search')
    results = []

    if query:
        # Perform a search query on your Product model
        results = Product.objects.filter(product_name__icontains=query)

    context = {'results': results, 'query': query}
    


    return render(request , 'Product/templates/Product_search.html' , context)


# def product_search(request):
#     query = request.GET.get('query')
#     results = []

#     if query:
#         # Perform a search query on your Product model
#         results = Product.objects.filter(name__icontains=query)

#     context = {'results': results, 'query': query}
#     return render(request, 'search.html', context)