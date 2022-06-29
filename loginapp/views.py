# Django Imports
import datetime
from django.http import HttpResponse
from django.shortcuts import  render, redirect
import pytz

from loginapp.models import UserLog
from .forms import NewUserForm, UserLogForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Local Imports
# from .forms import ContactUsForm

# Create your views here.

def DashboardView(request):

    return render(request, 'loginapp/dashboard.html')


def LoginView(request):
    if request.method == 'POST' and 'btnform1' in request.POST:
        form1 = NewUserForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            login(request, user)
            login_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

            messages.success(
                request, 'Registration successful.')
            return render(request, 'loginapp/dashboard.html', context={"login_time":login_time})
        messages.error(request, "Unsuccessful registration. Invalid information.")

    if request.method == "POST" and 'btnform2' in request.POST:
        form2 = AuthenticationForm(request, data=request.POST)
        if form2.is_valid():
            login_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            
            username = form2.cleaned_data.get('username')
            password = form2.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, 'loginapp/dashboard.html', context={"login_time":login_time})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form1 = NewUserForm()
    form2 = AuthenticationForm()
    # context = {'form': form}
    return render(request, 'loginapp/login.html', context={"register_form":form1, "login_form":form2})

def UserLogView(request):
    if request.method == 'POST':
        # form = UserLogForm(request.POST)
        username = request.POST['username']
        session_time = request.POST['session_time']
        login_time = request.POST['login_time']
        logout_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

        userlog = UserLog(username=username,session_time=session_time, login_time = login_time, logout_time = logout_time)
        userlog.save()
    return HttpResponse('success')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("loginapp:login")
 
        
