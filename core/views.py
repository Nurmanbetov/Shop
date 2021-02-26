from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from allauth.account.views import signup
from .forms import ProfileEditForm
from core import forms




def sign_out(request):
    auth.logout(request)
    return redirect(signup)





def edit_profile(request, pk):
    profile = User.objects.get(id=pk)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("goods")

    context = {}
    context["form"] = ProfileEditForm(instance=profile)

    return render(
        request,
        "enroll/home.html",
        context
    )

