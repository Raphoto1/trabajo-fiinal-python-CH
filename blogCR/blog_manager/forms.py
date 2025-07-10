from django import forms
from .models import Blog

class CreateBlogEntryForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)