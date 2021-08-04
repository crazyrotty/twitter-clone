from django import forms
from django.forms import fields
from tweet_app.models import Tweet


class TweetForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea)

    
    class Meta:
        model = Tweet
        fields = ['body',]