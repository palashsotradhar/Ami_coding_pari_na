from .models import login,regimodel
from django import forms

class loginform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'PassWord'}))
    class Meta:
        model = login
        fields = '__all__'

class regiform(forms.ModelForm):
    class Meta:
        model = regimodel
        fields = '__all__'
    #i set same widget for all fields

    def __init__(self, *args, **kwargs):
        super(regiform, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    #after that i need to set some different widget for password and email so i overwrite it...
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
