from django.db import models
from Home.models import CustomUser


# Create your models here.

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE , null = True)
    doctor_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    specialisation = models.CharField(max_length=255)
    doctor_image = models.ImageField(upload_to='doctor_image' ,null=True)
    experience = models.CharField(max_length=1000)
    schedule_time = models.DateTimeField(auto_now=True)
    clinic_name = models.CharField(max_length=255)
    clinic_address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=20, null=True , default='481001')

    def __str__(self):
        return self.doctor_name
    
    @property
    def imageURL(self):
        try:
            url=self.doctor_image.url
        except:
            url=''
        return url
    




class Appointment(models.Model):
    Appointment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , null=True)
    Doctor_pid = models.ForeignKey(Doctor, on_delete=models.CASCADE , null=True , blank=True)
    Name  = models.CharField(max_length=255 , null=True)
    Number  = models.IntegerField(null=True)
    Number  = models.IntegerField(null=True)
    Appointment_Date = models.DateTimeField()
    Appointment_time = models.TimeField()



    def __str__(self):
        return f"{self.Doctor_pid.doctor_name} "#-  - {self.user.username}"
    












    # 13.	Appointment
# a.	Appointment_id , primary key
# b.	User_id (Foreign key)
# c.	Doctor_id(Foreign key)
# d.	Appointment_Date(DataTime)
# e.	Appointment_time(TIME)