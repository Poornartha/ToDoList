from django import forms
from django.forms import ModelForm

from .models import *


class NewCustomer(forms.ModelForm):

    class Meta:
        model = Consumer
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-lg-9'}),
            'password': forms.PasswordInput(),
        }


class NewForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-lg-9'}),
        }


class Delete(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'complete']

