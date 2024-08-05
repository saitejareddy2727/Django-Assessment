from django import forms
class CommentForm(forms.Form):
    Author = forms.CharField(max_length = 255)
    text = forms.CharField(max_length=255)