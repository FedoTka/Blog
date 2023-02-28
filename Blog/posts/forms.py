from django import forms
from .models import *
class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    def self(self):
        new_tag =Tag.objects.create(title=self.cleaned_data['title'],
                                    slug = self.cleaned_data['slug'])
        return new_tag



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'slug', 'Post_text', 'image']
