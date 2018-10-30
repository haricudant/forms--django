from django import forms

class FormNames(forms.Form):
    Name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
