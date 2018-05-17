from backend.services import SearchService
from django.views import View
from django.shortcuts import redirect, render

class Search(View):
    search = SearchService()

    def get(self, req):
        criteria = req.GET.get('criteria', False)

        if not criteria:
            return redirect('/web')
        customers, orders = self.search.search(criteria)

        return render(req, 'search.html', {'customers': customers[:10],
                                           'orders': orders[:10],
                                           'criteria': criteria})