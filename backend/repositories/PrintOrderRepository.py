from backend.models.PrintOrderModel import PrintOrder
from .AbstractRepository import AbstractRopository


class PrintOrderRepository(AbstractRopository):
    model = PrintOrder
