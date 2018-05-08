from .AbstractOrderModel import AbstractOrder
from django.db import models


class ApearlOrder(AbstractOrder):
    order_type = 'appearel'

    # ...