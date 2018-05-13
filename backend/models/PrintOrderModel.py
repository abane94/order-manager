from .AbstractOrderModel import AbstractOrder
from django.db import models


class PrintOrder(AbstractOrder):
    order_type = 'print'
    oder_type = models.CharField(default='print9')


    def __str__(self):
        return u'%d' % self.id

    weight_choices = (
        ("20Lb", '20'),
        ("30Lb", '30'),
        ("50Lb", '50'),
    )

    material_choices = (
        ("CardStock", 'cardstock'),
        ("Gloss", 'gloss'),
        ("News", 'news'),
    )

    double_sided = models.BooleanField(default=False)
    # ink colors how to model
    material_color = models.CharField(max_length=20) # Choices?
    weight = models.CharField(max_length=20, choices=weight_choices) #  int?
    size = models.CharField(max_length=20)  # maybe need and x and y
    original_size = models.CharField(max_length=20)  # maybe choices

    quantity = models.IntegerField()
    material = models.CharField(max_length=20, choices=material_choices)  # Need this?

    stapled = models.BooleanField(default=False)
    padded = models.BooleanField(default=False)
    # pads_of = models.CharField(max_length=20)  # What is this?
    # cut to...?
    folding = models.BooleanField(default=False)
    collated = models.BooleanField(default=False)
    scoring = models.BooleanField(default=False)
    # starting_no = models.IntegerField()
