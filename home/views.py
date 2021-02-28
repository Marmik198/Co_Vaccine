from datetime import *
from random import randint

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import Appointment
from geo import models
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def home(request):
    return render(request, 'home/home.html')

@login_required
def appointment(request):
    secrets = {
        'reCAPTCHA_SITE_KEY' : '6Le8KmsaAAAAAFWZbyWkSif5hdy6iyxV9ONlLern',
        'all_incidences' : models.Incidences.objects.all()
    }
    return render(request, 'home/appointment.html' ,secrets)

def appointment_form_submission(request):
    firstName = request.POST['firstName']
    lastname = request.POST['lastname']
    aadhar = request.POST['aadhar']
    contact = request.POST['contact']
    age = request.POST['age']
    gender = request.POST['gender']
    Flatno = request.POST['Flatno']
    Address = request.POST['Address']
    City = request.POST['City']
    State = request.POST['State']
    Country = request.POST['Country']
    medical_issues = request.POST.getlist('meds[]')
    current_symptom = request.POST.getlist('symptoms[]')
    covid_status = request.POST['radio']
    travel_history = request.POST['radio-1']
    date = request.POST['date']
    dose = request.POST['dose']
    desc = request.POST['desc']
    center = request.POST['center']
    image = request.FILES['image']
    user = request.user

    appointmentForm = Appointment(user=user,firstName=firstName,lastname=lastname,aadhar=aadhar,contact=contact,age=age,gender=gender,
                                   Flatno=Flatno,Address=Address,City=City,State=State,Country=Country,medical_issues=medical_issues
                                   ,current_symptom=current_symptom,covid_status=covid_status,travel_history=travel_history,date=date,dose=dose,desc=desc,center=center,image=image)
    appointmentForm.save()
    messages.success(request,f'Your Appointment has been booked.')

    curr_date =  datetime.today().strftime('%Y-%m-%d')
    c1 = datetime.today()

    curr_date1 = c1+timedelta(days=1)
    curr_date1_formatted = curr_date1.strftime('%Y-%m-%d')

    curr_date2 = (curr_date1  + timedelta(days=1))
    curr_date2_formatted = curr_date2.strftime('%Y-%m-%d')

    curr_date3 = (curr_date2  + timedelta(days=1))
    curr_date3_formatted = curr_date3.strftime('%Y-%m-%d')

    curr_date4 = (curr_date3  + timedelta(days=1))
    curr_date4_formatted = curr_date4.strftime('%Y-%m-%d')

    curr_date5 = (curr_date4  + timedelta(days=1))
    curr_date5_formatted = curr_date5.strftime('%Y-%m-%d')

    curr_date6 = (curr_date5  + timedelta(days=1))
    curr_date6_formatted = curr_date6.strftime('%Y-%m-%d')

    obj = models.Incidences.objects.get(name=appointmentForm.center)
    obj_name = obj.name
    if curr_date == appointmentForm.date:
        temp = obj.todays
        print(obj.todays)
        temp=temp-1
        if(temp<0):
            return redirect('home')
        obj.todays = temp
        obj.save()
    elif curr_date1_formatted == appointmentForm.date:
        temp = obj.ones
        temp=temp-1
        if(temp<0):
            return redirect('home')
        obj.ones = temp
        obj.save()
    elif curr_date2_formatted ==appointmentForm.date:
        temp = obj.two
        temp=temp-1
        if(temp<0):
            return redirect('home')
        obj.two = temp
        obj.save()
    elif curr_date3_formatted == appointmentForm.date:
        temp = obj.three
        temp=temp-1
        if(temp<0):
            return redirect('home')
        obj.three = temp
        obj.save()
    elif curr_date4_formatted == appointmentForm.date:
        temp = obj.four
        temp=temp-1
        if(temp<0):
            return redirect('home')
        obj.four = temp
        obj.save()
    elif curr_date5_formatted==appointmentForm.date:
        temp = obj.five
        temp=temp-1
        if(temp<0):
            return redirect('home')
        obj.five = temp
        obj.save()

    success(request, obj_name)
    return render(request, 'home/home.html')

def faq(request):
    return render(request, 'home/faq.html')

def success(request,  obj):
    uniqueId = 'GR'
    for i in range(0, 9):
        uniqueId = uniqueId + str(randint(0, 9))
    template = render_to_string('home/email_template.html', {'name': request.user.username, 'rand':uniqueId})
    email = EmailMessage(
        'Thanks',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently = False
    email.send()


