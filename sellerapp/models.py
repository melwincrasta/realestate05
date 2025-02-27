# Create your models here.
from django.db import models
from userapp.models import CustomUser

class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_pic/', blank=True, null=True)

    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return self.name
