from django.shortcuts import render, redirect
from django.views import View
from backend.models import AbstractOrder, PrintOrder
from backend.services import PrintService, CustomerService
from datetime import datetime

from backend.forms import NewPrintForm


class Order(View):

    def get(self, req, id=0):
        id = self.kwargs.get('id', False)
        if not id:
            return redirect('/web')
            pass
        order = AbstractOrder.objects.get(id=id)
        type = order.get_type()
        print('order type: ' + type)
        if type == 'print':
            order = PrintOrder.objects.get(id=id)
            pass
        elif type == 'sign':
            pass

        return render(req, type + '.html', {'order': order, 'type': type})
