'''
*************************************************************************************************************

    File name: views.py
    Project: todo application using HTML  and DRF

    Discription of this file: This file is use to handel the control function.
  
**************************************************************************************************************
'''


from tkinter.tix import Form
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from apptodo import forms
from apptodo.forms import TODOForm
from apptodo.models import TODO
from django.contrib.auth.decorators import login_required
from django.contrib import messages


'''
#########################################################################################
#    function Name:  home
#########################################################################################
#    Description:  This function shows the login page once the user requested.
#########################################################################################
#    Input:   
#        1. request - user for authentication 
#########################################################################################
#    output: return login page.
#########################################################################################
'''

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})

'''
#########################################################################################
#    function Name:  login
#########################################################################################
#    Description:  This function is use to validate the user.
#########################################################################################
#    Input:   
#        1. request - user name.
#        2. request - password.
#########################################################################################
#    output: If login successful it redirect to home page and if not then it gives warning.
#########################################################################################
'''

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request , 'login.html' , context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
            
        else:
            context = {
            "form" : form
        }
        return render(request , 'login.html' , context=context)


'''
#########################################################################################
#    function Name:  signup
#########################################################################################
#    Description:  This function is to add new user.
#########################################################################################
#    Input:   
#        1. request - User details
#########################################################################################
#    output: Save to Database and redirect to login page.
#########################################################################################
'''

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)

    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            user= form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)

'''
#########################################################################################
#    function Name:  add_todo
#########################################################################################
#    Description:  This function is use to add new task.
#########################################################################################
#    Input:   
#        1. request - Title , Status , Priority.
#########################################################################################
#    output: Task saved in database and display in the table.
#########################################################################################
'''

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            # form = TODOForm()
            return render(request , 'index.html' , context={'form' : form})

'''
#########################################################################################
#    function Name:  delete
#########################################################################################
#    Description:  This function is use to delete the task.
#########################################################################################
#    Input:   
#        1. request - selected task.
#########################################################################################
#    output: Removed from database.
#########################################################################################
'''

def delete_todo(request, id):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home')

'''
#########################################################################################
#    function Name:  change_todo
#########################################################################################
#    Description:  This function is use to change the todo task and save.
#########################################################################################
#    Input:   
#        1. request - get id.
#########################################################################################
#    output: return home page.
#########################################################################################
'''

def change_todo(request, id, status):
    print(id)
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

'''
#########################################################################################
#    function Name:  signout
#########################################################################################
#    Description:  This function is use to logout the user from the current session.
#########################################################################################
#    Input:   
#        1. request - signout.
#########################################################################################
#    output: return login page.
#########################################################################################
'''

def signout(request):
    logout(request)
    return redirect('login')