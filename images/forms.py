from django import forms
from .models import Image, Comment
from urllib import request
from django.utils.text import slugify
from django.core.files.base import ContentFile


class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('title', 'description', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

