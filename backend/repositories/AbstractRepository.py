from enum import Enum

class Modifers(Enum):
    CONTAINS = '__contains'
    ICONTAINS = '__icontains'
    pass


class AbstractRopository:

    model = NotImplementedError

    def getById(self, id):
        return self.model.objects.get(id=id)
        pass

    def get(self, criteria):
        return self.model.objects.get(**criteria)

    def filter(self, criteria=[], all=True, items=0, offset=0):
        has_more = False
        if not isinstance(criteria, (list,)):
            criteria = [criteria]
        query = self.model.objects.all()
        has_more_query = self.model.objects.all()
        for data in criteria:
            if data.get('method', '') == 'order_by':
                # data.pop('method', None)
                query = query.order_by(data['field'])
                has_more_query = has_more_query.order_by(data['field'])
            else:
                query = query.filter(**data)
                has_more_query = has_more_query.filter(**data)

        if not all:
            total_len = len(self.model.objects.all())
            after_offset = offset + items
            has_more_query = has_more_query[after_offset: after_offset + 1]
            has_more = len(has_more_query) # TODO: check for login error, imutibility
            query = query[offset: offset + items]
        return query, has_more

    # def recently_updated(self, items=10, offset=0, all=False):
    #     has_more = False
    #     if not all:
    #         records = self.model.objects.all()[offset:items]
    #         has_more = bool(self.model.objects.all()[offset + items:1])
    #     else:
    #         records = self.model.objects.all()  # [offset:items]
    #
    #     return records, has_more

    def recently_updated(self, items=10, offset=0, all=False):
        filter_criteria = [
            {
                'method': 'order_by',
                'field': 'updated'
            }
        ]
        return self.filter(filter_criteria, all, items, offset)

    def recently_created(self, items=10, offset=0, all=False):
        filter_criteria = [
            {
                'method': 'order_by',
                'field': 'created'
            }
        ]
        return self.filter(filter_criteria, all, items, offset)

