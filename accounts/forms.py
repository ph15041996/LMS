from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book_Taker

class registrationform(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput,label="Enter Password")

    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password1"]
        exclude = ["date_joined"]

class loginform(forms.Form):
    username = forms.CharField(label="Enter Username")
    password = forms.CharField(widget=forms.PasswordInput,label="Enter Password")
    

class profileform(forms.ModelForm):
    
    class Meta:
        model = Book_Taker
        fields = ["user","fee_paid"]
        exclude = ["paid_date","member_till"]