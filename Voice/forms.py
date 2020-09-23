from django import forms 
from .models import *
  
class SignatureForm(forms.ModelForm): 
    class Meta: 
        model = Signature 
        fields = ['sign_upload'] 