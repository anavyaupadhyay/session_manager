from django.urls import path
from django.contrib.auth.views import  PasswordChangeView

from .views import LoginView, DashboardView, UserLogView, logout_request

app_name = "loginapp"

urlpatterns = [
    path('', LoginView, name='login'),
    path('dashboard', DashboardView, name='dashboard'),
    path('userlog', UserLogView, name='UserLogs'),
    path('logout', logout_request, name='logout'),
    
]