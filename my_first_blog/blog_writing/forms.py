from .models import Post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class PostForms(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'date', 'img']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок записи'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор статьи'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            # 'img': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'изображение'}),
        }
