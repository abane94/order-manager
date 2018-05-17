from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from datetime import datetime
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class Signin(View):
    def post(self, req):
        user = authenticate(username=req.POST['user'], password=req.POST['pass'])
        if user is not None:
            login(req, user)
        url = req.POST.get('redirect', '/web')
        return redirect(url)

class Signout(View):
    def get(self, req):
        logout(req)
        return redirect('/web')

class Password(View):

    def get(self):
        pass

    def post(self):
        pass