from django.db import models



class Good(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0)

    def __str__(self):
        return self.name

  