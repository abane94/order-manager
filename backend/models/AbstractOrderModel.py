from django.db import models
from django.contrib.auth.models import User
from .CustomerModel import CustomerModel

class AbstractOrder(models.Model):
    # class Meta:
    #     abstract = True

    order_type = ''

    QUOTE = 'QUOTE'
    ORDER = 'ORDER'
    COMPLETED = 'COMPLETED'
    ARCHIVED = 'ARCHIVE'
    status_choices = (
        (QUOTE, 'QUOTE'),
        (ORDER, 'ORDER'),
        (COMPLETED, 'COMPLETED'),
        (ARCHIVED, 'ARCHIVED'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(choices=status_choices, max_length=10)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    quote = models.IntegerField()   # dollars
    quote_date = models.DateField()
    order_date = models.DateField()
    due_date = models.DateField()
    # completed / archived date ?
    deposite = models.IntegerField() # cents
    final_price = models.IntegerField # cents
    balance = models.IntegerField() # cents
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # TODO: import and add User Model
    notes = models.TextField()
    need_approval = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)  # TODO: default?
    payment_due_date = models.DateField()
    updated = models.DateField()
    created = models.DateField()

    # def __init__(self):
    #     raise NotImplementedError

    # Name
    # Description
    # Status: QUOTE / ORDER / COMPLETE
    # Customer: Customer
    # Quote
    # Date
    # Order
    # Date
    # Due
    # Date
    # Completed / Archived
    # Date ? (different from due date)
    # Deposit
    # Quoted
    # price
    # Final
    # price
    # Balance
    # Filled
    # Out
    # By: User
    # Notes
    # Need
    # approval
    # Approved
    # Payment
    # due
    # date
