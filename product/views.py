from django import forms
from django.shortcuts import render, redirect   
from product.models import *
from product.forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Q



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

def category(request, pk):
    context = {}
    category = Category.objects.get(id=pk)
    context["goods"] = Good.objects.filter(
        Q(category__id=pk) |
        Q(category__in=category.child_category.all()),
        available=True,
    )
    context["category_pk"] = pk
    return render(request, "good/goods.html", context)



class CategoryCreate(CreateView):
    model = Category
    fields = ["name"]
    template_name = "good/create_category.html"
    success_url = reverse_lazy("goods")