from django.db.models import Q

from backend.models import CustomerModel, AbstractOrder


class SearchService:

    special_chars = ['.', ',', '/']

    def search(self, criteria):
        criteria = str(criteria).replace('  ', ' ').strip()
        for ch in self.special_chars:
            criteria.replace(' ' + ch, ' ')
            criteria.replace(ch + ' ', ' ')
        terms = criteria.split(' ')

        # search customers
        query = Q()
        for term in terms:
            query = query | Q(name__icontains=term)
            query = query | Q(company__icontains=term)
            query = query | Q(address__icontains=term)
            query = query | Q(city__icontains=term)
            query = query | Q(email__icontains=term)
        customers = CustomerModel.objects.filter(query).order_by('updated')

        # search orders
        query = Q()
        for term in terms:
            query = query | Q(name__icontains=term)
            query = query | Q(description__icontains=term)
            query = query | Q(notes__icontains=term)
        orders = AbstractOrder.objects.filter(query).order_by('updated')

        return customers, orders
