from .AbstractOrderModel import AbstractOrder
from django.db import models


class PrintOrder(AbstractOrder):
    order_type = 'print'

    double_sided = models.BooleanField(default=False)
    # ink colors how to model
    material_color = models.CharField(max_length=20) # Choices?
    weight = models.CharField(max_length=20) #  int?
    size = models.CharField(max_length=20)  # maybe need and x and y
    original_size = models.CharField(max_length=20)  # maybe choices

    quantity = models.IntegerField()
    material = models.CharField(max_length=20)  # Need this?

    stappeled = models.BooleanField(default=False)
    padded = models.BooleanField(default=False)
    pads_of = models.CharField(max_length=20)  # What is this?
    # cut to...?
    folding = models.BooleanField(default=False)
    collated = models.BooleanField(default=False)
    scoring = models.BooleanField(default=False)
    starting_no = models.IntegerField()
