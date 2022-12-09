"""Forms of the project."""

from django import forms

from things.models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={
                'max_length': '35'
            }),
            'description': forms.Textarea(attrs={
                'max_length': '120'
            }),
            'quantity': forms.NumberInput(attrs={
                'type': 'number',
                'min': '0',
                'max': '50'
            })
        }