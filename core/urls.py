from django.urls import path
from .views import *

urlpatterns = [
    path("sign-out/", sign_out, name="sign-out"),
]