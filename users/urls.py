from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('verify-email/', views.verify_email_page, name='verify-email'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]