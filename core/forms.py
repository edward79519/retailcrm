from django import forms
from django.forms import formset_factory

from .models import Company
from .validator import FileValidator
from django.utils.translation import gettext_lazy as _


class AddCustomForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('fullname', 'shortname', 'sn', 'stock_id', 'source', 'sponsor', 'author')
        # fields = '__all__'
        labels = {
            'fullname': '公司名稱*',
            'shortname': '公司簡稱*',
            'sn': '統一編號*',
            'stock_id': '上市代碼',
            'source': '客戶來源',
            'sponsor': '負責人',
            'author': '',
        }
        help_texts = {
            'fullname': '輸入公司完整名稱。ex. 寶晶能源股份有限公司',
            'shortname': '輸入公司簡稱，方便辨識。',
            'sponsor': '選擇我方負責人員。',
        }
        error_messages = {

        }
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'FullName',
                'required': True,
            }),
            'shortname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ShortName',
                'required': True,
            }),
            'sn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID',
                'required': True,
            }),
            'stock_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Stock_ID',
            }),
            'source': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Source',
            }),
            'sponsor': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Sponsor',
                'required': True,
            }),
            'author': forms.HiddenInput(),
        }


class UpdateCustomForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('is_draft', 'is_open')
        labels = {
            'fullname': '公司名稱*',
            'shortname': '公司簡稱*',
            'sn': '統一編號*',
            'stock_id': '上市代碼',
            'source': '客戶來源',
            'sponsor': '負責人',
            'category': '產業別',
            'rank': '客戶等級',
            'status': '客戶狀態',
            'addr_county': '公司地址',
            'addr_detail': '公司地址',
            'website': '公司網站',
            'contact_name': '主要聯絡人',
            'contact_title': '職稱',
            'contact_tel': '聯絡電話',
            'contact_email': '聯絡信箱',
            'pwr_usage': '年用電量',
            'pwr_inquire': '需求量',
            'unit_price': '報價',
            'duration': '合約年限',
            'report': 'CSR/ESG 報告',
            'warn_date': '重要日期',
            'remark': '備註',
            'author': '',
        }
        help_texts = {
            'fullname': '輸入公司完整名稱。ex. 寶晶能源股份有限公司',
            'shortname': '輸入公司簡稱，方便辨識。',
            'sponsor': '選擇我方負責人員。',
        }
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control-plaintext',
                'readonly': True,
            }),
            'shortname': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'rank': forms.Select(attrs={
                'class': 'form-control',
            }),
            'sn': forms.TextInput(attrs={
                'class': 'form-control-plaintext',
                'readonly': True,
            }),
            'stock_id': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'source': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'addr_county': forms.Select(attrs={
                'class': 'form-control',
            }),
            'addr_detail': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'contact_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'contact_title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'contact_tel': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'contact_email': forms.TextInput(attrs={
                'type': 'email',
                'class': 'form-control',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
            }),
            'report': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'pwr_usage': forms.NumberInput(attrs={
                'class': 'form-control text-end',
            }),
            'pwr_inquire': forms.NumberInput(attrs={
                'class': 'form-control text-end',
            }),
            'unit_price': forms.NumberInput(attrs={
                'class': 'form-control text-end',
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control text-end',
            }),
            'warn_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'remark': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'sponsor': forms.Select(attrs={
                'class': 'form-control',
            }),
            'author': forms.HiddenInput(),
        }

    field_order = ['fullname', 'shortname', 'sn', 'stock_id']


class UpdatePWRInfoForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('status', 'pwr_usage', 'pwr_inquire', 'unit_price', 'duration', 'warn_date')
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
            }),
            'pwr_usage': forms.NumberInput(attrs={
                'class': 'form-control text-end',
                'aria-describedby': 'basic-addon2',
                'min': 0,
                'max': 9999999999,
                'step': 0.1,
            }),
            'pwr_inquire': forms.NumberInput(attrs={
                'class': 'form-control text-end',
                'aria-describedby': 'basic-addon2',
                'min': 0,
                'max': 9999999999,
                'step': 0.1,
            }),
            'unit_price': forms.NumberInput(attrs={
                'class': 'form-control text-end',
                'aria-describedby': 'basic-addon2',
                'min': 0,
                'max': 99,
                'step': 0.01,
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control text-end',
                'aria-describedby': 'basic-addon2',
                'min': 0,
                'max': 99,
                'step': 1,
            }),
            'warn_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
        }


class XlsUploadForm(forms.Form):
    source_validator = FileValidator(
        ("xlsx",),
        ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/zip"),
        max_size=1 * 1024 * 1024, )

    source_file = forms.FileField(
        required=True,
        max_length=100,
        validators=[source_validator],
        label=_("上傳檔案"),
        help_text=_("副檔名為 .xlsx, 檔名不能超過 100 字元"),
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'required': True,
            'accept': '.xlsx',
        })
    )


CreatFormset = formset_factory(AddCustomForm)
