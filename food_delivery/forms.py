from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    date_of_birth = forms.DateField(required=False)
    expected_salary = forms.DecimalField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'mobile', 'email', 'address', 'date_of_birth', 'expected_salary')
