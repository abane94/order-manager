from django.contrib import admin
from django.urls import path
from Web.views.views import index, CustomerActions, Customer
from Web.views import PrintActions, Print, Order, Search
from Web.views import Signin, Signout
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('', index),
    path('customer/form/<int:id>/', CustomerActions.as_view()),
    path('customer/form/', CustomerActions.as_view(), {"id": 0}),
    path('customer/<int:id>/', Customer.as_view()),
    path('customer/', Customer.as_view(), {'id': 0}),
    path('order/', index),


    path('order/print/form/<int:id>/', PrintActions.as_view()),
    path('order/print/form/', PrintActions.as_view(), {"id": 0}),
    path('order/print/<int:id>/', Print.as_view()),
    path('order/print/', Print.as_view(), {'id': 0}),

    path('order/<int:id>/', Order.as_view()),
    path('order/', Order.as_view(), {'id': 0}),

    path('auth/signin/', Signin.as_view()),
    path('auth/signout/', Signout.as_view()),
    path('auth/password/', PasswordChangeView.as_view(success_url='/web', template_name='password.html')),

    path('search/', Search.as_view())
]