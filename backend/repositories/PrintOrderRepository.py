from backend.models.PrintOrderModel import PrintOrder
from .AbstractRepository import AbstractRopository


class OrderRopository(AbstractRopository):
    model = PrintOrder
