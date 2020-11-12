from django import forms
from django.forms import fields
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_code','full_name','mobile','role')
        labels = {
            'full_name': 'Full Name',
            'emp_code':'Employee Code',
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['role'].empty_label = "Select"
        self.fields['emp_code'].required = False