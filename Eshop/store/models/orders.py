from django.db import models
from django.db.models.deletion import CASCADE
from .product import Product
from .customer import Customer
import datetime


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=10,default='')
    date = models.DateField(default=datetime.datetime.today)



    def placeOrder(self):
        self.save()
    
   