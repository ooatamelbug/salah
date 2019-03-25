from django.db import models

# Create your models here.

# Create Model for depart.
class Depart(models.Model):
    token = models.CharField(max_length=200,default='8dcb8ea967601761113feb25d24b477e331fff4e')
    name = models.CharField(max_length=100)
    """docstrDepart"""
    def __str__(self):
        return self.name



# Create Model for product .
class Products(models.Model):
    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    discount = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    discounttime = models.DateField(auto_now=False)
    describ = models.TextField()
    token = models.CharField(max_length=200,default='8dcb8ea967601761113feb25d24b477e331fff4e')
    depart = models.ForeignKey('Depart',on_delete=models.CASCADE)
    """docstrDepart"""
    def __str__(self):
        return self.name



# Create Model for image .
class Images(models.Model):
    token = models.CharField(max_length=200,default='8dcb8ea967601761113feb25d24b477e331fff4e')
    link = models.ImageField(default='default.png',blank=True)
    products = models.ForeignKey('Products',on_delete=models.CASCADE)
