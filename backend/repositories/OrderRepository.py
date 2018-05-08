from backend.models.AbstractOrderModel import AbstractOrder
from .AbstractRepository import AbstractRopository


class OrderRopository(AbstractRopository):
    model = AbstractOrder
