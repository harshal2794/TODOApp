'''
*************************************************************************************************************

    File name: urls.py
    Project: todo application using HTML  and DRF

    Discription of this file: This file is use to route to the template of the application.
  
**************************************************************************************************************
'''

from cgitb import html
from http.client import HTTPResponse
from django.contrib import admin
from django.urls import path
from apptodo.views import home, login, signup, signout, add_todo, delete_todo, change_todo


urlpatterns = [
    path('' , home , name='home'),
    path('login/' , login , name='login'),
    path('signup/' , signup),
    path('logout/' , signout),
    path('add-todo/' , add_todo),
    path('delete-todo/<int:id>' , delete_todo),
    path('change-status/<int:id>/<str:status>' , change_todo),
]
