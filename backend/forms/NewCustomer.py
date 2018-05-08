from backend.models import CustomerModel
from django import forms
from django.forms import ValidationError
from datetime import datetime


class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"
        exclude = ("id", "last_in", "last_user")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.NumberInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control'}),

            'folder_location': forms.TextInput(attrs={'class': 'form-control'}),
            'needs_followup': forms.CheckboxInput(attrs={'class': 'form-control'}),  # attrs={'class': 'form-control'}

            # 'last_user': forms.HiddenInput(),
            # 'last_in': forms.HiddenInput(),  # might not be needed
            'updated': forms.HiddenInput(),
            'created': forms.HiddenInput(),
        }

    # def clean_name(self):
    #     print('name')
    #     return self.cleaned_data['name']
    # def clean_company(self):
    #     print('company')
    #     return self.cleaned_data['company']
    # def clean_phone(self):
    #     print('phone')
    #     return self.cleaned_data['phone']
    # def clean_email(self):
    #     print('email')
    #     return self.cleaned_data['email']
    # def clean_name(self):
    #     print('name')
    #     return self.cleaned_data['name']
    # def clean_name(self):
    #     print('name')
    #     return self.cleaned_data['name']
    # def clean_name(self):
    #     print('name')
    #     return self.cleaned_data['name']
    # def clean_name(self):
    #     print('name')
    #     return self.cleaned_data['name']

    # def clean_updated(self):
    #     print('updated')
    #     return datetime.now().date()
    #
    # def clean_created(self):
    #     print('created')
    #     return datetime.now().date()