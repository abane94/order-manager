from django.shortcuts import render, redirect
from django.views import View
from backend.services import HomeService, CustomerService
from datetime import datetime

from django.contrib.auth.models import User

# move to services or repos
from backend.forms import NewCustomerForm, EditCustomerForm

# Create your views here.
home = HomeService()
customers = CustomerService()


def index(req):
    # do some auth stuff
    followup_page = int(req.GET.get('followup_page', 0))
    orders_page = int(req.GET.get('order_page', 0))
    data = home.get(followup_page=followup_page, orders_page=orders_page)
    return render(req, 'home.html', data)

class CustomerActions(View):

    def get(self, req, id=0):
        action = req.GET.get('action', '')
        if action == 'edit':
            customer = customers.getById(id=self.kwargs['id'])
            form = EditCustomerForm(instance=customer, initial={'id': customer.id, 'updated': datetime.now().date()})  # TODO: should be edit_customer_form, set the current user to the form
            return render(req, 'customerForm.html', {'form': form, 'action': 'edit', 'id': id})
        else:
            form = NewCustomerForm(initial={'updated': datetime.now().date(), 'created': datetime.now().date()})  # TODO: set the current user in the form fileds
            return render(req, 'customerForm.html', {'form': form, 'action': 'new'})  # , 'id': req.GET['id']})

    def post(self, req, id=0):
        # create / update student
        action = req.POST.get('action', '')
        if action == 'edit':
            customer = customers.getById(id=self.kwargs['id'])
            form = EditCustomerForm(req.POST, instance=customer)  # TODO: edit form
            form.save()
            return redirect('/web')
        elif action == 'delete':
            customer = customers.getById(id=self.kwargs['id'])
            customer.delete()
            return redirect('/web')
        else:
            form = NewCustomerForm(req.POST)
            form.save()
            return redirect('/web')
        pass


class Customer(View):

    def get(self, req, id=0):
        id = self.kwargs.get('id', False)
        if not id:
            return redirect('/web')
            pass
        customer = customers.getById(id)
        orders = customers.ordersOf(customer)
        for order in orders:
            print('hello')

        return render(req, 'customer.html', {'customer': customer, 'orders': orders})
