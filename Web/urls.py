from django.contrib import admin
from django.urls import path
from Web.views.views import index, CustomerActions, Customer

urlpatterns = [
    path('', index),
    path('customer/form/<int:id>/', CustomerActions.as_view()),
    path('customer/form/', CustomerActions.as_view(), {"id": 0}),
    path('customer/<int:id>/', Customer.as_view()),
    path('customer/', Customer.as_view(), {'id': 0}),
    path('order/', index)
]