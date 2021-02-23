from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse



def goods(request):
    return HttpResponse("List of Goods")