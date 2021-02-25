from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from allauth.account.views import signup



def sign_out(request):
    auth.logout(request)
    return redirect(signup)


