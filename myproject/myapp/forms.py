from django import forms
from .models import Register







class RegisterForm(forms.ModelForm):
    
    class Meta:
        
        model = Register
        fields = ['first_name','last_name','username','email','password','contact']
        widgets = {
            'password': forms.PasswordInput(),
        }
    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact.isdigit():
            raise forms.ValidationError("Contact number must contain digits only.")
        if len(contact) != 10:
            raise forms.ValidationError("Contact number must be exactly 10 digits.")
        if contact.startswith('0'):
            raise forms.ValidationError("Contact number should not start with 0.")
        return contact

  

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)