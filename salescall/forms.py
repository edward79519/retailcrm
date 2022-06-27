from django import forms
from django.forms.models import inlineformset_factory

from .models import CallRecord, Participants, Comment


class AddCallRecordForm(forms.ModelForm):
    class Meta:
        model = CallRecord
        fields = '__all__'


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ['name', 'side', 'title']
        widgets = {
            'name': forms.TextInput(
                attrs={'required': True}
            ),
            'side': forms.CheckboxInput(),
            'title': forms.TextInput(
                attrs={'required': True}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['id', 'content']


ParticipantFormset = inlineformset_factory(
    CallRecord,
    Participants,
    ParticipantForm,
    can_delete=True,
    extra=3,
    max_num=10,
)
