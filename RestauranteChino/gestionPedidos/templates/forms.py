from django import forms
from .models import cleintes


class AutoForm(forms.ModelForm):
    class Meta:
        model = cleintes
        fields = ['nombre', 'direccion', 'direccion', 'email', 'telefono']