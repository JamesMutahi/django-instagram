from django import forms
from .models import Post

# ......
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
