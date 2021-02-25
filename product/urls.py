from product.context_processor import category
from django.urls import path 
from .views import *
from allauth.account import views

urlpatterns = [
    path("all/", goods, name="goods"),
    path("create/", create_good, name="create-good"),
    path("category/<int:pk>/", category, name="category"),
    path("category/create/", CategoryCreate.as_view(), name="category-create" ),
    path("<int:pk>/", GoodDetailView.as_view(), name="good"),
    path("", views.signup, name="account_signup"),
]