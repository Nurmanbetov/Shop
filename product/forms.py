from django import  forms
from product.models import Good


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