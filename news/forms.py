from .models import Article
from django.forms import ModelForm, TextInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
                'style': 'border: 1px solid black;'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание статьи',
                'style': 'border: 1px solid black;'
            })
        }