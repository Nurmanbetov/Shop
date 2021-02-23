from product.context_processor import category
from django.urls import path 
from .views import *

urlpatterns = [
    path("all/", goods, name="goods"),
    path("<int:id>/", good, name="good"),
    path("create/", create_good, name="create-good"),
    path("category/<int:pk>/", category, name="category"),
    path("category/create/", CategoryCreate.as_view(), name="category-create" )
]