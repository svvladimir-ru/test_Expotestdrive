from django.db import models
from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text", "image", "file")

        labels = {
            "text": "Текст записи",
            "image": "Изображение",
            "file": "Файл",
        }



