from django.db import models

# Create your models here.

class Depart(models.Model):
    name = models.CharField(max_length=100)
    """docstrDepart"""
    def __str__(self):
        return self.name


class User(models.Model):
    """docstring forUser."""
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    stat = models.IntegerField(default=1)
    """docstrDepart"""
    def __str__(self):
        return self.name



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



class Images(models.Model):
    link = models.ImageField(default='default.png',blank=True)
    products = models.ForeignKey('Products',on_delete=models.CASCADE)
