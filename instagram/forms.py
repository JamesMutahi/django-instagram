from django import forms
from .models import *


# ......
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('name', 'image', 'bio')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
