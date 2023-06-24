from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ["image"]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': False, 'accept': 'image/png, image/jpg, image/jpeg', 'id': 'images', 'type': 'file', 'required': True}),
        }