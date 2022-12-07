import re

from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['massage', 'photo', 'tag_set', 'is_public'] #'__all__'
        #fields = '__all__'
        #비추천
        #exclude = ''

    def clean_massage(self):
        massage = self.cleaned_data.get('massage')
        if massage:
            massage = re.sub(r'[a-zA-Z]+', '', massage)
        return massage