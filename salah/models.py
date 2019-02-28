from django.db import models

# Create your models here.

# Create Model for depart.
class Depart(models.Model):
    name = models.CharField(max_length=100)
    """docstrDepart"""
    def __str__(self):
        return self.name



# Create Model for product .
class Products(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    discount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    discounttime = models.DateField(auto_now=False)
    describ = models.TextField()
    depart = models.ForeignKey('Depart',on_delete=models.CASCADE)
    """docstrDepart"""
    def __str__(self):
        return self.name



# Create Model for image .
class Images(models.Model):
    link = models.ImageField(default='default.png',blank=True)
    products = models.ForeignKey('Products',on_delete=models.CASCADE)
