from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    about = models.TextField(max_length=500, null=False)
    photo = models.FileField(upload_to='products/', null=False)
    price = models.FloatField(null=False, default=1111)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return str(self.name)
