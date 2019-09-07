from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import UserProfile

def index(request):
    return render(request, 'index.html')

def signUpView(request):
    username = request.POST['Username']
    password = request.POST['Password']
    email = request.POST['Email']

    user = User.objects.create_user(username, email, password)
    user.save()

    return render(request, 'signup.html')

def loginView(request):
    username = request.POST['Username']
    password = request.POST['Password']

    user = authenticate(request, username=username, password=password)

    data = None
    
    if user is not None:
        login(request, user)
        data = UserProfile.objects.filter(userid=request.user)
        print(data)
    return render(request, 'login.html', {'data': data})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

def userProfileView(request, link):
    return render(request, 'profile.html')

def userMessage(request):
    userid = request.POST['profileid']
    message = request.POST['message']
    userdata = UserProfile.objects.create(userid=userid, message=message)
    userdata.save()
    return render(request, 'thankyou.html')
