from django.shortcuts import render , redirect
from Shop.models import ShopOwner
from Product.models import Product , Product_Category

# Create your views here.
def Shop(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        sadd = request.POST.get('sadd')
        snumber = request.POST.get('snumber')
        scity = request.POST.get('scity')
        sstate = request.POST.get('sstate')
        spin = request.POST.get('spin')

        com=ShopOwner(shop_name = sname,phone_number=snumber, full_address=sadd , state=sstate,city=scity, pin_code=spin)
        com.save()
        return redirect('/Shop/dashboards')
    
   

    return render(request , 'Shop_registration.html' )

def dashboards(request):
    shopp = ShopOwner.objects.all()

    context={
          'shopp':shopp
    }
    print(context)
    return render(request , 'dashboard.html' , context)


def insert(request):
     if request.method == 'POST':
        product_name = request.POST.get('product_name')
        cat_id = request.POST.get('cat_id')
        product_image = request.FILES.get('productImage')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock_quantity = request.POST.get('stock_quantity')
        status = request.POST.get('status')

        print(f"Received data: product_name={product_name}, cat_id={cat_id}, product_image={product_image}, description={description}, price={price}, stock_quantity={stock_quantity}, status={status}")



        if not cat_id or not cat_id.isdigit():
            categories = Product_Category.objects.all()
            return render(request, 'error.html', {'error': 'Invalid Category ID', 'categories': categories})
        
        # Ensure cat_id is a valid Product_Category instance
        try:
            category = Product_Category.objects.get(cat_id=cat_id)
        except Product_Category.DoesNotExist:
            return render(request, 'insert_data.html', {'error': 'Invalid Category ID', 'categories': Product_Category.objects.all()})
        
        # Create a new product
        product = Product(
            product_name=product_name,
            # url_slug=slugify(product_name),
            cat_id=category,
            product_image=product_image,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            status=status
        )
        product.save()
        return redirect('/')  # Redirect to a success page

     categories = Product_Category.objects.all()


     return render(request , 'inser_data.html' ,{'categories': categories})
# def registration(request):
#     return render(request , 'Shop_registration.html')