from django.shortcuts import render
from .forms import UserCreateForm
#from django.contrib.auth.forms import UserCreationForm
#These next imports create a new user in admin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupaccount(request):
    if request.method=='GET':
        return render(request, 'signupaccount.html', {'form':UserCreateForm})
    else:
        if request.method=='POST':
            password = request.POST['password1']
        if len(password)<8:
            return render(request, 'signupaccount.html',
                          {'form': UserCreateForm, 'error': 'passwords must be atleast 8 characters'})
        if password.isdigit():
            return render(request, 'signupaccount.html',
                          {'form': UserCreateForm, 'error': 'passwords must contain other characters'})
        if password != request.POST['password2']:
            return render(request, 'signupaccount.html',
                          {'form': UserCreateForm, 'error': 'passwords do not match'})

        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],
                                          password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signupaccount.html', {'form':UserCreateForm,
                                                             'error': 'Username already taken. choose another one' })


        else:
            return render(request, 'signupaccount.html',
                  {'form': UserCreateForm, 'error':'passwords do not match'})


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',
                      {'form': AuthenticationForm})
    else:
        user= authenticate(request,
                           username=request.POST['username'],
                           password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html',
                          {'form':AuthenticationForm(),
                           'error': 'username and password donot match'})
        else:
            login(request,user)
            return redirect('home')

