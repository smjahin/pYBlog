from django import forms
from django.forms import widgets
from blog.models import Post, Category, Comment

choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'content')

        widgets = {

            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is place holder'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'content')
        widgets = {

            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is place holder'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {

            
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }