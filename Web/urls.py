from django.contrib import admin
from django.urls import path
from Web.views.views import index, CustomerActions, Customer
from Web.views import PrintActions

urlpatterns = [
    path('', index),
    path('customer/form/<int:id>/', CustomerActions.as_view()),
    path('customer/form/', CustomerActions.as_view(), {"id": 0}),
    path('customer/<int:id>/', Customer.as_view()),
    path('customer/', Customer.as_view(), {'id': 0}),
    path('order/', index),


    path('order/print/form/<int:id>/', PrintActions.as_view()),
    path('order/print/form/', PrintActions.as_view(), {"id": 0}),
    # path('order/print/<int:id>/', Customer.as_view()),
    # path('order/print/', Customer.as_view(), {'id': 0}),
]