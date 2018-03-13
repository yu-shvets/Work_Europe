from django import forms
from .models import Messages


class MessageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['mail'].widget.attrs['placeholder'] = 'Your email'
        self.fields['message'].widget.attrs['placeholder'] = 'Write your message'

    class Meta:
        model = Messages
        fields = ('mail', 'message')


