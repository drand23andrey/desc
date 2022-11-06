from django import forms

class CreateTaskForm(forms.Form):
    theme = forms.CharField(label='Тема', max_length=100)
    text = forms.CharField(label='Текст', max_length=3000)