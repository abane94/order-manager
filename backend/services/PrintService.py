from backend.repositories import PrintOrderRepository

class PrintService():

    prints = PrintOrderRepository()

    def recent_quotes(self, items=10, offset=0, all=False):
        # return data, has_more
        pass

    def active_ordes(self, items=10, offset=0, all=False):
        # return data, has_more
        pass

    def getById(self, id):
        return self.prints.getById(id)
    # pass through methods to the repository