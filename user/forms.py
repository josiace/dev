from django import forms

class Inscription(forms.Form):
    nom = forms.CharField(max_length=30)
    prenom = forms.CharField(max_length=10)
    mail = forms.EmailField()
