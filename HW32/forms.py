from django import forms
from captcha.fields import CaptchaField

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()