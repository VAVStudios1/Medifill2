from django.shortcuts import render
from Contact.models import FeedBack

# Create your views here.
def feedback(request):
   
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        description = request.POST.get('feedback')
        feedback=FeedBack(name = fname,email=email, number=number , description=description)
        feedback.save()
       
    

 
    return render(request , 'Contact/templates/feedback.html')