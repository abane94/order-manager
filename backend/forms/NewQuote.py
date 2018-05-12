from backend.models import AbstractOrder
from django import forms
from django.forms import ValidationError
from datetime import datetime


class NewQuote(forms.ModelForm):
    class Meta:
        model = AbstractOrder
        fields = "__all__"
        exclude = ("id",
                   "last_in",
                   "last_user",
                   "order_date",
                   "due_date",
                   'deposite',
                   'final_price',
                   'balance',
                   'need_approval',
                   'approved',
                   'payment_due_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-md'}),
            'quote': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'notes': forms.Textarea(attrs={'class': 'form-control form-control-md'}),

            # 'last_user': forms.HiddenInput(),
            # 'last_in': forms.HiddenInput(),  # might not be needed
            'customer': forms.HiddenInput(),
            'status': forms.HiddenInput(),
            'updated': forms.HiddenInput(),
            'created': forms.HiddenInput(),
            'quote_date': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
        }
