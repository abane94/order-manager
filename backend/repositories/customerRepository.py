from backend.models.CustomerModel import CustomerModel
from .AbstractRepository import AbstractRopository, Modifers


class CustomerRopository(AbstractRopository):
    model = CustomerModel

    # argument expansion:
    # def foo(a=1, b=2, c=3):
    #     print
    #     a, b, c
    #
    # data = {
    #     'a': 5,
    #     'c': 9
    # }
    # foo(**data)  # output: 5 2 9

    #Entry.objects.all()[5:10]
    # [offset:limit]

    # def recently_updated(self, items=10, offset=0, all=False):
    #     has_more = False
    #     if all:
    #         records = CustomerModel.objects.all()[offset:items]
    #         has_more = bool(CustomerModel.objects.all()[offset + items:1])
    #     else:
    #         records = CustomerModel.objects.all()[offset:items]
    #
    #     return records, has_more

    # def _recently_updated(self, items=10, offset=0, all=False):
    #     filter_criteria = [
    #         {
    #             'method': 'order_by',
    #             'field': 'updated'
    #         }
    #     ]


    # have functions for each field, that will have a switch for each modifier
    # name
    # company
    # phone
    # email
    # address
    # city
    # zip
    # balance
    # last_user = models.ForeignKey(User)
    # last_in
    # folder_location
    # needs_followup
    # updated
