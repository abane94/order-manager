from backend.models import SignOrder
from .AbstractRepository import AbstractRopository


class SignOrderRepository(AbstractRopository):
    model = SignOrder
