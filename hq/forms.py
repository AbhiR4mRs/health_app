from django import forms
from .models import PublicContent

class PublicContentForm(forms.ModelForm):
    class Meta:
        model = PublicContent
        fields = ['title', 'content_type', 'text_content', 'file']
        widgets = {
            'content_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CreateCenterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    center_name = forms.CharField(max_length=100)
    is_subcenter = forms.BooleanField(required=False, label='Is Subcenter?')
