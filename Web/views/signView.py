from django.shortcuts import render, redirect
from django.views import View
from backend.services import SignService, CustomerService
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from backend.forms import NewSignForm, EditSignForm

signs = SignService()
customers = CustomerService()


class SignActions(View, LoginRequiredMixin):

    def get(self, req, id):
        action = req.GET.get('action', '')
        if action == 'edit':
            sign = signs.getById(id=self.kwargs['id'])
            form = EditSignForm(instance=sign, initial={'id': sign.id,
                                                                'updated': datetime.now().date()})  # TODO: should be edit_customer_form, set the current user to the form
            return render(req, 'orderForm.html', {'form': form, 'action': 'edit', 'id': id, 'type': 'sign'})
        else:
            customer = req.GET['customer']
            form = NewSignForm(initial={'updated': datetime.now().date(),
                                            'created': datetime.now().date(),
                                            'quote_date': datetime.now().date(),
                                            'status': 'QUOTE',
                                            'customer': customers.getById(customer)})  # TODO: set the current user in the form fileds
            return render(req, 'orderForm.html', {'form': form, 'action': 'new', 'type': 'sign'})  # , 'id': req.GET['id']})

    def post(self, req, id=0):
        # create / update student
        action = req.POST.get('action', '')
        if action == 'edit':
            sign = signs.getById(id=self.kwargs['id'])
            form = EditSignForm(req.POST, instance=sign)  # TODO: edit form
            form.save()
            return redirect('/web')
        elif action == 'delete':
            sign = signs.getById(id=self.kwargs['id'])
            sign.delete()
            return redirect('/web')
        else:
            form = NewSignForm(req.POST)
            form.save()
            return redirect('/web')
        pass


class Sign(View):

    def get(self, req, id=0):
        id = self.kwargs.get('id', False)
        if not id:
            # return redirect('/web')
            quotes_page = int(req.GET.get('quotes_page', 0))
            orders_page = int(req.GET.get('order_page', 0))
            ctx = signs.get(quotes_page=quotes_page, orders_page=orders_page)
            ctx['type'] = 'Sign'
            return render(req, 'orderHome.html', ctx)
            pass
        order = signs.getById(id)

        return render(req, 'sign.html', {'order': order, 'type': 'sign'})
