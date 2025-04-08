from django.shortcuts import render , redirect
from Doctor.models import Doctor , Appointment
from Product.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def Doctors(request):
    query1 = request.GET.get('search1')
    query2 = request.GET.get('search2').strip() if request.GET.get('search2')  else None
    results = []
    
    
    if query1:
        print("Query 1:", query1)
        results += Doctor.objects.filter(doctor_name__icontains=query1 )
    if query2:
        print("Query 2:", query2)
        results += Doctor.objects.filter(specialisation__icontains=query2)

    context = {'results': results, 'query1': query1, 'query2': query2}
    print("Results:", results)
    print(context)


        
    return render(request , 'Search_Dr.html' , context )

def dr_profile(request , doctor_name):
    doctor = Doctor.objects.get(doctor_name=doctor_name)
    context = {'doctor': doctor}
    print(context)
    return render(request , 'Dr_profile.html' ,context )


def appointment(request):
     if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        user = request.user
        # doctor = request.user.doctor  # Assuming user has a related Doctor object

        # Create Appointment object
        appointment = Appointment.objects.create(
            user=user,
            # Doctor_pid=doctor,
            Name=name,
            Number=number,
            Appointment_Date=appointment_date,
            Appointment_time=appointment_time
        )
        appointment.save()


     return render(request , 'appointment.html')
@login_required
def registration(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('dname')
        phone_number = request.POST.get('dnum')
        specialisation = request.POST.get('dspec')
        experience = request.POST.get('dexp')
        doctor_image = request.FILES.get('doctor_image')
        clinic_name = request.POST.get('dclin')
        clinic_address = request.POST.get('dadd')
        state = request.POST.get('state')
        city = request.POST.get('city')
        user = request.user

        com=Doctor(doctor_name = doctor_name,user_id=user,phone_number=phone_number,doctor_image=doctor_image, specialisation=specialisation , experience=experience,
                   clinic_name=clinic_name, clinic_address=clinic_address , state=state ,city=city)
        com.save()
        return redirect('/Doctor/dashboard')
   
    return render(request , 'Dr_registration.html')
def dashboard(request):
   
    return render(request , 'drdashboard.html')