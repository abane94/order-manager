from .AbstractOrderModel import AbstractOrder
from django.db import models

class SignOrder(AbstractOrder):

    order_type = 'sign'

    quantity = models.IntegerField()
    width = models.IntegerField()  # inches?
    height = models.IntegerField()  # inches?
    material = models.CharField(max_length=40)
    double_sided = models.BooleanField(default=False)
    gromets = models.BooleanField(default=False)  # TODO: check data type
    sewing = models.BooleanField(default=False)  # TODO: check data type
    webbing = models.BooleanField(default=False)  # TODO: check data type
    tape = models.BooleanField(default=False)  # TODO: check data type
    corner_rounding = models.BooleanField(default=False)  # TODO: check data type