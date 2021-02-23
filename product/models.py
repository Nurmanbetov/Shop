from django.db import models



class Good(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, default=0, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(to="Category", related_name="good", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name

    