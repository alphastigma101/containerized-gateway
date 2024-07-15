from django import forms

class CreateTableForm(forms.Form):
    name = forms.CharField(label='Table Name', max_length=30)
    description = forms.CharField(label='Table Description', widget=forms.Textarea)
