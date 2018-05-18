from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminView(View, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser()

    def get(self, req):
        users = User.objects.all()

        return render(req, 'admin.html', {'users': users})