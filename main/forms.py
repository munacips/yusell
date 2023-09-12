from turtle import textinput
from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Search...','type':'search'}),label='')