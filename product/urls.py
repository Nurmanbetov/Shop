from django.urls import path 
from .views import goods 

urlpatterns = [
    path("all/", goods, name="goods")
]