from django import forms
from .models import Company


class AddCustomForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['fullname', 'shortname', 'sn', 'stock_id', 'source', 'sponsor', 'author']
        # fields = '__all__'
        widgets = {
            'fullname': forms.TextInput(),
            'shortname': forms.TextInput(),
            'sn': forms.TextInput(),
            'stock_id': forms.TextInput(),
            'source': forms.Select(),
            'sponsor': forms.Select(),
            'author': forms.Select(),
        }


class UpdateCustomForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
