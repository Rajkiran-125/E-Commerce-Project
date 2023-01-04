from django import forms
from .models import SignupModel,LoginModel,CustomerModel


class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields = "__all__"

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password'}) 
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = "__all__"

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password'}) 
        }
        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['name','phone','locality','city','zipcode']

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter name'}),
            'phone':forms.NumberInput(attrs={'placeholder':'Enter phone number'}),
            'locality':forms.TextInput(attrs={'placeholder':'Enter locality'}),
            'city':forms.TextInput(attrs={'placeholder':'Enter city'}),
            'zipcode':forms.NumberInput(attrs={'placeholder':'Enter zipcode'})

        }
        
