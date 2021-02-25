from typing import KeysView
from django import forms
from django.forms.utils import from_current_timezone
from django.shortcuts import render, redirect   
from product.models import *
from product.forms import *
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def goods(request):
    context = {} 
    context["goods"] = Good.objects.filter(available=True)
    return render(request, "good/goods.html", context)

#def good(request, id):
#    context = {}
#    context["good"] = Good.objects.get(id=id)
#    return render(request, "good/good.html", context)



class GoodDetailView(DetailView):
    template_name = "good/good.html"
    model = Good

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data( **kwargs)
        good = Good.objects.get(id=self.kwargs["pk"])
        breadcrumbs = []
        category = good.category 
        while True:
            if category:
                breadcrumbs = [category] + breadcrumbs
                category = category.parent_category
            else:
                break
        context["breadcrumbs"] = breadcrumbs
        return context


@login_required(login_url="login")
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