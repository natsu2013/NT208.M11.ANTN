from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=50)

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)
