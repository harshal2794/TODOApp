'''
*************************************************************************************************************

    File name: urls.py
    Project: todo application using HTML  and DRF

    Discription of this file: This file is use to route to the todo application.
  
**************************************************************************************************************
'''

from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('apptodo.urls'))
]
