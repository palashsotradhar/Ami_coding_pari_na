from .models import khojm
from django import forms

class khojform(forms.ModelForm):
    input_values = forms.CharField(label='Take Your Value',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Input'}))
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search'}))

    class Meta:
        model = khojm
        fields = ('input_values','search',)