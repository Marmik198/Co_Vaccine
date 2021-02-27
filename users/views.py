import jwt
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.forms import UserRegisterForm
from users.utils import Util


def register(request):
    if(request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relativeLink = reverse('login')
            absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
            email_body = 'Hi ' + user.username + ' use link below to verify your email \n' + absurl
            data = {
                'to': email,
                'email_body': email_body,
                'email_subject': 'Verify your email'
            }
            Util.send_email(data)
            return redirect('verify-email')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def verify_email_page(request):
    return render(request, 'users/verify-email-page.html')

def reset_password(request):
    return render(request, 'users/reset_password.html.html')


