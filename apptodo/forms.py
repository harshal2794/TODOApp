'''
*************************************************************************************************************

    File name: forms.py
    Project: todo application using HTML  and DRF

    Discription of this file: This is a file containing the model form for which form module is imported 
    from the libraries and the required fields are assign in the form.
  
**************************************************************************************************************
'''


from django.forms import ModelForm
from apptodo.models import TODO


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'priority' ]
