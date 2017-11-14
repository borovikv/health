from django import forms
from log.models import Event


class EventForm(forms.models.ModelForm):
    class Meta:
        model = Event
        exclude = []
        widgets = {'type': forms.HiddenInput(), 'subject': forms.HiddenInput()}
