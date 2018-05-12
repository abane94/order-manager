from django.db import models
from django.contrib.auth.models import User
from .CustomerModel import CustomerModel

class AbstractOrder(models.Model):
    # class Meta:
    #     abstract = True

    def __str__(self):
        return str(self.id)

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
    quote = models.IntegerField(default=0)   # dollars
    quote_date = models.DateField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    # completed / archived date ?
    deposite = models.IntegerField(default=0) # cents
    final_price = models.IntegerField(default=0) # cents
    balance = models.IntegerField(default=0) # cents
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # TODO: import and add User Model
    notes = models.TextField(blank=True, null=True)
    need_approval = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)  # TODO: default?
    payment_due_date = models.DateField(blank=True, null=True)
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
