from django import forms
from recipebox.models import Author


class RecipesForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time = forms.CharField(max_length=25)
    description = forms.CharField(max_length=140)
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorsForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
