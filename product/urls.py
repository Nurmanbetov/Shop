from django.urls import path 
from .views import *

urlpatterns = [
    path("all/", goods, name="goods"),
    path("<int:id>/", good, name="good"),
    path("create/", create_good, name="create-good"),
]