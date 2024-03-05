from django.db import models

class Account_Details(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    Email = models.CharField(max_length=50)
    Contact_no=models.IntegerField(12)
    Address=models.TextField()
    Password=models.TextField()

class Product(models.Model):
    picture = models.ImageField(upload_to='product_pics/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)



