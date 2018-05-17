from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User


class AdminView(View):

    def get(self, req):
        users = User.objects.all()

        return render(req, 'admin.html', {'users': users})