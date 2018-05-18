from backend.models import PrintOrder
from django import forms
from .NewQuote import NewQuote


class EditPrintForm(forms.ModelForm):

    class Meta():
        model = PrintOrder
        fields = "__all__"
        exclude = ("id",
                       "last_in",
                       "last_user",
                        "name",
                   
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
            # 'status': forms.Input,
            'updated': forms.HiddenInput(),
            'created': forms.HiddenInput(),
            'quote_date': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),

            # 'statue': forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-md'}),
            #     required=True,
            #     widget=forms.TextInput,
            #     choices=PrintOrder.status_choices,
            # ),

            "order_date": forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-md'}),
            "due_date": forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-md'}),
            'deposite': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'final_price': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),


            'double_sided': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'material_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-md'}),
            # 'weight': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control form-control-md'}),
            'size': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'original_size': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),
            # 'material': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'stapled': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'padded': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'folding': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'collated': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            'scoring': forms.CheckboxInput(attrs={'class': 'form-control form-control-md'}),
            # 'starting_no': forms.NumberInput(attrs={'class': 'form-control form-control-md'}),

            # 'last_user': forms.HiddenInput(),
            # 'last_in': forms.HiddenInput(),  # might not be needed
        }

        # status = forms.ComboField(
        #     choices=PrintOrder.status_choices,
        #     required=True
        # )
