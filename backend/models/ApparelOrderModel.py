from .AbstractOrderModel import AbstractOrder
from django.db import models


class ApearlOrder(AbstractOrder):
    order_type = 'appearel'

    def __unicode__(self):
        return u'%d' % self.id

    # ...