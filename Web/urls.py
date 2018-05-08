from django.contrib import admin
from django.urls import path
from Web.views.views import index, CustomerActions

urlpatterns = [
    path('', index),
    path('customer/form', CustomerActions.as_view()),
    path('order/', index)
]