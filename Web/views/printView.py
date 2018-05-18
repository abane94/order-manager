from django.shortcuts import render, redirect
from django.views import View
from backend.services import PrintService, CustomerService
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from backend.forms import NewPrintForm, EditPrintForm

prints = PrintService()
customers = CustomerService()


class PrintActions(View, LoginRequiredMixin):

    def get(self, req, id):
        action = req.GET.get('action', '')
        if action == 'edit':
            print = prints.getById(id=self.kwargs['id'])
            form = EditPrintForm(instance=print, initial={'id': print.id,
                                                                'updated': datetime.now().date()})  # TODO: should be edit_customer_form, set the current user to the form
            return render(req, 'customerForm.html', {'form': form, 'action': 'edit', 'id': id, 'type': 'print'})
        else:
            customer = req.GET['customer']
            form = NewPrintForm(initial={'updated': datetime.now().date(),
                                            'created': datetime.now().date(),
                                            'quote_date': datetime.now().date(),
                                            'status': 'QUOTE',
                                            'customer': customers.getById(customer)})  # TODO: set the current user in the form fileds
            return render(req, 'orderForm.html', {'form': form, 'action': 'new', 'type': 'print'})  # , 'id': req.GET['id']})

    def post(self, req, id=0):
        # create / update student
        action = req.POST.get('action', '')
        if action == 'edit':
            print = prints.getById(id=self.kwargs['id'])
            form = EditPrintForm(req.POST, instance=print)  # TODO: edit form
            form.save()
            return redirect('/web')
        elif action == 'delete':
            print = prints.getById(id=self.kwargs['id'])
            print.delete()
            return redirect('/web')
        else:
            form = NewPrintForm(req.POST)
            form.save()
            return redirect('/web')
        pass


class Print(View):

    def get(self, req, id=0):
        id = self.kwargs.get('id', False)
        if not id:
            # return redirect('/web')
            quotes_page = int(req.GET.get('quotes_page', 0))
            orders_page = int(req.GET.get('order_page', 0))
            ctx = prints.get(quotes_page=quotes_page, orders_page=orders_page)
            ctx['type'] = 'Print'
            return render(req, 'orderHome.html', ctx)
            pass
        order = prints.getById(id)

        return render(req, 'print.html', {'order': order, 'type': 'print'})

