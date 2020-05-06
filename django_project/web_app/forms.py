from django import forms  
from .models import Signup1
      
class ApplicationForm(forms.ModelForm):  
    class Meta:  
        model = Signup1  
        fields = ['full_name','gender','phone_no','email','resume_file'] 