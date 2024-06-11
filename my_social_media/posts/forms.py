from django import forms

from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model =  Post
        fields = ('text', 'image')
        widgets = {
            'text': forms.TextInput(attrs={"class":'post-form-inputs'}),
            'image': forms.ClearableFileInput(attrs={"class": 'post-form-img-input'})
        }
        labels = {
            'text': 'Post Text'
        }
