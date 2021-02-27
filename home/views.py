from django.shortcuts import render, redirect
from .models import Appointment

def home(request):
    return render(request, 'home/home.html')

def appointment(request):
    return render(request, 'home/appointment.html')

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
    dose = request.POST['dose']
    desc = request.POST['desc']
    image = request.FILES['image']

    appointmentForm = Appointment(firstName=firstName,lastname=lastname,aadhar=aadhar,contact=contact,age=age,gender=gender,
                                   Flatno=Flatno,Address=Address,City=City,State=State,Country=Country,medical_issues=medical_issues
                                   ,current_symptom=current_symptom,covid_status=covid_status,travel_history=travel_history,dose=dose,desc=desc,image=image)

    appointmentForm.save()
    return redirect('home')
