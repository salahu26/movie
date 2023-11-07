from django import forms
from . models import movies

class movieforms(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','des','year','img']