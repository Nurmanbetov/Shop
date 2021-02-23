from django import  forms
from django.forms import fields
from product.models import *


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = [
            "name",
            "category",
            "image",
            "description",
            "price"
        ]



class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]