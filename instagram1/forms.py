
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['massage', 'photo', 'tag_set', 'is_public'] #'__all__'
        #비추천
        #exclude = ''
