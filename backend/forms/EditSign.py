from backend.models import SignOrder
from django import forms
from .NewQuote import NewQuote

class EditSignForm(forms.ModelForm):
    class Meta(NewQuote):
        model = SignOrder
        fields = "__all__"
        exclude = ("id",
                        "name",
                       "last_in",
                       "last_user",

                       # "order_date",
                       # "due_date",
                       # 'deposite',
                       # 'final_price',
                       # 'balance',

                       'need_approval',
                       'approved',
                       'payment_due_date',
                        'order_type'
                   )

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control form-control-md'}),
            'quote': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'notes': forms.Textarea(attrs={'class': 'form-control form-control-md'}),

            # 'last_user': forms.HiddenInput(),
            # 'last_in': forms.HiddenInput(),  # might not be needed
            'customer': forms.HiddenInput(),
            # 'status': forms.HiddenInput(),
            'updated': forms.HiddenInput(),
            'created': forms.HiddenInput(),
            'quote_date': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),

            "order_date": forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-md'}),
            "due_date": forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-md'}),
            'deposite': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'final_price': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),

            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'width': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'height': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'material': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'double_sided': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'gromets': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'sewing': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'webbing': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'tape': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'corner_rounding': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
        }
