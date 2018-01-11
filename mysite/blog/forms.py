"""
Django comes with two base classes to build forms:
• Form: Allows you to build standard forms
• ModelForm: Allows you to build forms to create or update model instances
"""

from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        # indicate which model to use to build the form in the Meta class of the form
        model = Post   # Create a form based on Post model
        fields = ('author','title','text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author':forms.TextInput(attrs={'class': 'textinputclass'}),
            'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
