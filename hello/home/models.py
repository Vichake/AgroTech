from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=13)
    desc=models.TextField()

    def __str__(self):
        return self.name

class signup(models.Model):#login model
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password1=models.CharField(max_length=122)
    password2=models.CharField(max_length=122)


    def __str__(self):
        return self.username
    
class Sale(models.Model):
    ProductName=models.CharField(max_length=122)
    ProductDescription=models.CharField(max_length=122)
    ProductPrice=models.CharField(max_length=122)

    def __str__(self):
        return self.ProductName    