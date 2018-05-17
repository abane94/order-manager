from backend.repositories import CustomerRopository, OrderRopository
from backend.models import AbstractOrder

class CustomerService:

    customers = CustomerRopository()
    orders = OrderRopository()
    # customer is different b/c the home only shows the one table
    def recent_activity(self, itmes=20, offset=0, all=False):
        # return data, has_more
        pass

    # pass through methods to the repository

    def getById(self, id):
        return self.customers.getById(id)

    def ordersOf(self, customer):
        # return self.orders.filter({'customer': customer})
        return AbstractOrder.objects.filter(customer=customer)
