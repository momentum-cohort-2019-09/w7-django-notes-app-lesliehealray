from django import forms
from notes.models import Note, Comment


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'description']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
