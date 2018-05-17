from backend.repositories import PrintOrderRepository

class PrintService():

    prints = PrintOrderRepository()

    def recent_quotes(self, items=10, offset=0, all=False):
        filter_criteria = [
            {
                'status': 'QUOTE'  # use variables from models?
            },
            {
                'method': 'order_by',
                'field': 'updated'
            }
        ]
        return self.prints.filter(filter_criteria, all, items, offset)

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
        return self.prints.filter(filter_criteria, all, items, offset)

    def getById(self, id):
        return self.prints.getById(id)
    # pass through methods to the repository


    def get(self, quotes_page=0, orders_page=0):
        ret = {}
        ret['orders'], ret['more_orders'] = self.active_orders(10, 10 * orders_page)
        # ret['orders'], ret['more_orders'] = self.active_orders(10, 10 * orders_page)

        link = 'quote_page=' + str(quotes_page) + '&order_page='
        if ret['more_orders']:
            ret['orders_next_link'] = link + str(orders_page + 1)
        if orders_page > 0:
            ret['orders_prev_link'] = link + str(orders_page - 1)

        ret['quotes'], ret['more_quotes'] = self.recent_quotes(10, 10 * quotes_page)

        link = 'order_page=' + str(orders_page) + '&quotes_page='
        if ret['more_quotes']:
            ret['quotes_next_link'] = link + str(quotes_page + 1)
        if quotes_page > 0:
            ret['quotes_prev_link'] = link + str(quotes_page - 1)
        return ret
