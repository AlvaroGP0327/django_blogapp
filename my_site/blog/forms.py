from django import forms
from .models import User, Role

#Formulario para registro de usuario

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
    
    username = forms.CharField(max_length=64,required=True,
                               widget=forms.TextInput(attrs={'class':'form-control'})
                               )
    
    