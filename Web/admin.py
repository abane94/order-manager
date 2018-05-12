from django.contrib import admin

from backend.models import CustomerModel, AbstractOrder, PrintOrder
# Register your models here.

admin.site.register(CustomerModel)
admin.site.register(AbstractOrder)
admin.site.register(PrintOrder)