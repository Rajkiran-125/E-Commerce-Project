from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomerModel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    phone = models.IntegerField(max_length=50)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('M','Manswear'),
    ('W','Womanswear'),
    ('A','Accessories'),
    ('N','NewArrivals'),
    ('F','Featured')
)

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.CharField(max_length=50)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES ,max_length=5)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    

class OrderPlacedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
 

class SignupModel(models.Model):
    username = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class LoginModel(models.Model):
    username = models.CharField(max_length=50,blank=True)
    password = models.CharField(max_length=50)






