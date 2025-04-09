from django.shortcuts import render , HttpResponse , redirect
from django.utils import timezone
from django.contrib.auth import login as log, authenticate
from django.contrib import messages
from django.contrib.auth.models import User 
import datetime
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# import google.generativeai as genai
from Contact.models import FeedBack
from Product.models import Product
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from Doctor.models import Doctor , Appointment
# custom_user_manager = CustomUserManager()

User = get_user_model()






# api_key = os.environ.get("GENAI_API_KEY")
# if not api_key:
#     raise ValueError("API key not found in environment variables")

# genai.configure(api_key=api_key)

# # Create the model
# generation_config = {
#     "temperature": 0.9,
#     "top_p": 1,
#     "top_k": 0,
#     "max_output_tokens": 2048,
#     "response_mime_type": "text/plain",
# }
# safety_settings = [
#     {
#         "category": "HARM_CATEGORY_HARASSMENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_HATE_SPEECH",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
#     {
#         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#     },
# ]

# model = genai.GenerativeModel(
#     model_name="gemini-1.0-pro",
#     safety_settings=safety_settings,
#     generation_config=generation_config,
# )

# chat_session = model.start_chat(
#     history=[]
# )






def index(request):
    products = Product.objects.all()
    results = Doctor.objects.all()
    # if request.method == 'POST':
    #      clear = request.POST('clear')
    #      if clear==True:
    #          if  request.session.session_key:
    #             request.session.flush()
    # if  request.session.session_key:
    #      request.session.flush()
 
    # if request.method == 'POST':
        
        
    #     user_message = request.POST.get('message')
       
    #     response = chat_session.send_message(user_message)


    #     request.session['chat_history'] = request.session.get('chat_history', []) + [
    #         {'role': 'user', 'text': user_message},
    #         {'role': 'MediBot', 'text': response.text},
    #     ]
    #     return redirect('/')
   
    # chat_history = request.session.get('chat_history', [])



    context = {
       # 'chat_history': chat_history,
        'products': products,
        'results': results,
    }

    print(context)
    return render(request, 'Home/templates/index.html' , context  )

def login(request):
   
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            log(request, user)
            # Redirect to a success page
            return redirect('/')  # Redirect to home page after successful login
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    else:

        

        return render(request, 'Home/templates/login.html' )
    
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('username')
        user = User.objects.create_user(email=email, password=password , first_name=fname )
        user.save()
        messages.success(request, f'Account created for {email}!')
        return redirect('/login')
      
        

        #return redirect('/')  # Redirect to login page after successful signup
    
    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def Profile(request):
    return render(request , 'Profile.html')

def returnq(request):
    return render(request , 'return.html')

def security(request):
    return render(request , 'security.html')

def change(request):
    return render(request , 'change_password.html')
def contact(request):
    return render(request , 'contact.html')
def aboutm(request):
    return render(request , 'about.html')

def privacy(request):
    return render(request , 'privacy_policy.html')

def myappointment(request):
    user_email = request.user.email
    # appoint = Appointment.objects.all()
    appoint = Appointment.objects.filter(user_id__email=user_email)
    context = {
        'appoint': appoint,
        
    }


    return render(request , 'myappointment.html' , context)


def feedback(request):
    if request.method == 'POST':
            fname = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            description = request.POST.get('feedback')
            feedback=FeedBack(name = fname,email=email, number=number , description=description)
            feedback.save()


    return render(request , 'feedback.html')






# @csrf_exempt
# def chatbot(request):
#     # if settings.SESSION_EXPIRE_AT_BROWSER_CLOSE and not request.session.session_key:
#     #     request.session.flush()
   

#     # if  request.session.session_key:
#     #     request.session.flush()

    


#     if request.method == 'POST':
#         user_message = request.POST.get('message')
#         response = chat_session.send_message(user_message)
#         request.session['chat_history'] = request.session.get('chat_history', []) + [
#             {'role': 'user', 'text': user_message},
#             {'role': 'MediBot', 'text': response.text},
#         ]
#         return redirect('chatbot')
   
#     chat_history = request.session.get('chat_history', [])
#     return render(request, 'chatbot.html', {'chat_history': chat_history})
