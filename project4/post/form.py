from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
    
    def save(self):
        return super().save(commit=False)
        # new_post.owner = user
        # print("ahihi", new_post.content, new_post.count_like, new_post.owner)
        # return new_post
# class PostForm(forms.Form):
#     content = forms.TextInput()
