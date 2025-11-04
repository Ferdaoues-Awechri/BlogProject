from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l’article'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'created_on': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
