from django import forms
from .models import City

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    source = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Select Source")
    destination = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Select Destination")
    travel_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('source')
        destination = cleaned_data.get('destination')
        
        if source and destination and source == destination:
            raise forms.ValidationError("Source and destination cannot be the same.")
        return cleaned_data