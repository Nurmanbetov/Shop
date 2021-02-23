from django.shortcuts import render 
from product.models import Good



def goods(request):
    context = {} 
    context["goods"] = Good.objects.filter(available=True)
    return render(request, "good/goods.html", context)