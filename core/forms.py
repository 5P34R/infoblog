from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        breakpoint()
        data = self.cleaned_data
        if data['username'] and data['email'] and data['password1'] and data['password2']: 
            if data['username'] == User.objects.filter(username=data['username']):
                self.add_error("Username already exists!")
            if data['email'] == User.objects.filter(username=data['email']):
                self.add_error("Email already exists!")
            if data['password1'] != data['password2']:
                self.add_error("Password doesnt match!")
        else:
            self.add_error("All fields are maditory")