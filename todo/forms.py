from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Add new task...'})
    )
