from backend.repositories import CustomerRopository
from backend.repositories import OrderRopository

class HomeService():
    def __init__(self):

        self.customers = CustomerRopository()
        self.orders = OrderRopository()

    def recent_quotes(self, items=10, offset=0, all=False):
        # return data, has_more
        # return self.orders.recently_updated(items, offset, all) # need to filter this to only quotes\
        filter_criteria = [
            {
                'status': 'QUOTE'  # use variables from models?
            },
            {
                'method': 'order_by',
                'field': 'updated'
            }
        ]
        return self.orders.filter(filter_criteria, all, items, offset)
        pass

    def active_orders(self, items=10, offset=0, all=False):
        filter_criteria = [
            {
                'status': 'ORDER'  # use variables from models?
            },
            {
                'method': 'order_by',
                'field': 'updated'  # order by order_date? by be by the inverse order
            }
        ]
        return self.orders.filter(filter_criteria, all, items, offset)
        # return data, has_more
        pass

    def needs_followup(self, items=10, offset=0, all=False):
        filter_criteria = [
            {
                'needs_followup': True
            },
            {
                'method': 'order_by',
                'field': 'updated'
            }
        ]
        return self.customers.filter(filter_criteria, all, items, offset)

    def get(self, quotes_page=0, followup_page=0, orders_page=0):
        ret = {}
        ret['orders'], ret['more_orders'] = self.recent_quotes(10, 10*quotes_page)
        # ret['orders'], ret['more_orders'] = self.active_orders(10, 10 * orders_page)
        print(len(ret['orders']))  # TODO: remove
        if ret['more_orders']:
            ret['recent_next_link'] = 'followup_page=' + str(followup_page) + '&order_page=' + str(orders_page + 1)
        if orders_page > 0:
            ret['recent_prev_link'] = 'followup_page=' + str(followup_page) + '&order_page=' + str(orders_page - 1)

        # followups, more_followup = self.needs_followup(10, 10 * followup_page)
        # ret['followups'] = followups
        # ret['more_followup'] = more_followup
        ret['followups'], ret['more_followup'] = self.needs_followup(10, 10 * followup_page)
        print(len(ret['followups']))  # TODO remove
        if ret['more_followup']:
            ret['followup_next_link'] = 'order_page=' + str(orders_page) + '&followup_page=' + str(followup_page + 1)
        if followup_page > 0:
            ret['followup_prev_link'] = 'followup_page=' + str(orders_page) + '&followup_page=' + str(followup_page - 1)
        return ret


    # pass through methods to the repository
