from django import forms
from .models import crudmodel


class crudform(forms.ModelForm):
    mycrud = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {
        'id':'todoField', 'placeholder':'Enter ToDo'
    }))
    class Meta:
        model = crudmodel
        fields = ['mycrud',]