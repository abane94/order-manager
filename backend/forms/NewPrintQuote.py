from backend.models import PrintOrder
from django import forms
from .NewQuote import NewQuote
from django.forms import ValidationError
from datetime import datetime


class NewPrintForm(forms.ModelForm):
    class Meta(NewQuote):
        model = PrintOrder
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


            'double_sided': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'material_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-md'}),
            'weight': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control form-control-md'}),
            'size': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'original_size': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'material': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'stapled': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'padded': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'folding': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'collated': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'scoring': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            # 'starting_no': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),

            # 'last_user': forms.HiddenInput(),
            # 'last_in': forms.HiddenInput(),  # might not be needed
        }
