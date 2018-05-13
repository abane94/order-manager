from django.shortcuts import render, redirect
from django.views import View
from backend.services import PrintService, CustomerService
from datetime import datetime

from backend.forms import NewPrintForm

prints = PrintService()
customers = CustomerService()


class PrintActions(View):

    def get(self, req, id):
        action = req.GET.get('action', '')
        if action == 'edit':
            customer = prints.getById(id=self.kwargs['id'])
            # form = EditCustomerForm(instance=customer, initial={'id': customer.id,
            #                                                     'updated': datetime.now().date()})  # TODO: should be edit_customer_form, set the current user to the form
            # return render(req, 'customerForm.html', {'form': form, 'action': 'edit', 'id': id})
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
            customer = prints.getById(id=self.kwargs['id'])
            # form = EditCustomerForm(req.POST, instance=customer)  # TODO: edit form
            # form.save()
            return redirect('/web')
        elif action == 'delete':
            # customer = prints.getById(id=self.kwargs['id'])
            # customer.delete()
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
            return redirect('/web')
            pass
        order = prints.getById(id)

        return render(req, 'print.html', {'order': order})