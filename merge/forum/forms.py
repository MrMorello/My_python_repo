from django.forms import ModelForm
from forum.models import Post, Thread


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        exclude = ['']


class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = ['']
