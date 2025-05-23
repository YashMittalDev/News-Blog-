from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = "Your Username"
        self.fields['username'].widgets = forms.TextInput()
        self.fields['email'].label = "Your Email"
        self.fields['email'].widgets = forms.EmailInput()
        self.fields['password1'].label = "Your Password"
        self.fields['password1'].widgets = forms.PasswordInput()
        self.fields['password2'].label = "Confirm Password"
        self.fields['password2'].widgets = forms.PasswordInput()
        
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

'''
class LoginForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = "Your Username"
        self.fields['username'].widgets = forms.TextInput()
        self.fields['password1'].label = "Password"
        self.fields['password1'].widgets = forms.PasswordInput()  
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username','password1']
'''

'''
class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())
'''
    