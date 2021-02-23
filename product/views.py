from django import forms
from django.shortcuts import render, redirect   
from product.models import Good
from product.forms import GoodForm



def goods(request):
    context = {} 
    context["goods"] = Good.objects.filter(available=True)
    return render(request, "good/goods.html", context)

def good(request, id):
    context = {}
    context["good"] = Good.objects.get(id=id)
    return render(request, "good/good.html", context)



def create_good(request):
    if request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(goods)
    context = {}
    context["form"] = GoodForm()
    return render(
        request,
        "good/form.html",
        context
    )
