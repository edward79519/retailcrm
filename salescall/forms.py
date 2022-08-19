from django import forms
from django.forms.models import inlineformset_factory

from .models import CallRecord, Participants, Comment


class AddCallRecordForm(forms.ModelForm):
    class Meta:
        model = CallRecord
        exclude = ('is_draft', 'is_open')
        labels = {
            'company': '客戶名稱',
            'calldate': '拜訪時間',
            'calltype': '接洽形式',
            'questions': '重要問題',
            'requirement': '需求詳述',
            'attachment': '相關附件',
            'summary': '訪問結果概要',
            'nextdate': '下次聯絡時間',
        }
        widgets = {
            'company': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'calldate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'calltype': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'questions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'requirement': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'attachment': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Report',
            }),
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'nextdate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'author': forms.HiddenInput(),
            'sn': forms.HiddenInput(),
        }


class UpdateCallRecordForm(forms.ModelForm):
    class Meta:
        model = CallRecord
        exclude = ('company', 'sn', 'is_draft', 'is_open')
        labels = {
            # 'company': '客戶名稱',
            'calldate': '拜訪時間',
            'calltype': '接洽形式',
            'questions': '重要問題',
            'requirement': '需求詳述',
            'attachment': '相關附件',
            'summary': '訪問結果概要',
            'nextdate': '下次聯絡時間',
        }
        widgets = {
            # 'company': forms.Select(attrs={
            #     'class': 'form-control',
            #     'required': True,
            # }),
            'calldate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'calltype': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'questions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'requirement': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'attachment': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Report',
            }),
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'nextdate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'author': forms.HiddenInput(),
        }


class FirstCallRecordForm(forms.ModelForm):
    class Meta:
        model = CallRecord
        exclude = ('is_draft', 'is_open')
        labels = {
            'company': '客戶名稱',
            'calldate': '拜訪時間',
            'calltype': '接洽形式',
            'questions': '重要問題',
            'requirement': '需求詳述',
            'attachment': '相關附件',
            'summary': '訪問結果概要',
            'nextdate': '下次聯絡時間',
        }
        widgets = {
            'company': forms.HiddenInput(),
            'calldate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'calltype': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'questions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'requirement': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'attachment': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Report',
            }),
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'nextdate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'author': forms.HiddenInput(),
            'sn': forms.HiddenInput(),
        }



class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ['name', 'side', 'title']
        widgets = {
            'name': forms.TextInput(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'side': forms.HiddenInput(),
            'title': forms.TextInput(
                attrs={'required': True, 'class': 'form-control'}
            ),
        }
        labels = {
            'name': '姓名',
            'side': '',
            'title': '職稱',
        }


class PartiUpdateForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ['id', 'name', 'side', 'title']
        widgets = {
            'id': forms.HiddenInput(),
            'name': forms.TextInput(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'side': forms.HiddenInput(),
            'title': forms.TextInput(
                attrs={'required': True, 'class': 'form-control'}
            ),
        }
        labels = {
            'name': '姓名',
            'side': '',
            'title': '職稱',
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
    extra=1,
    max_num=10,
)


PartiUpdateFormset = inlineformset_factory(
    CallRecord,
    Participants,
    PartiUpdateForm,
    extra=1,
    max_num=10,
)
