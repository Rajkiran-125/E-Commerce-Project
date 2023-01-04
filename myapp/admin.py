from django.contrib import admin
from .models import (
    CustomerModel,
    ProductModel,
    CartModel,
    OrderPlacedModel,
    SignupModel
)

# Register your models here.

@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','username','name','phone','locality','city','zipcode']

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price','size', 'description', 'brand', 'category','product_image']

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product','quantity']

@admin.register(OrderPlacedModel)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity']


@admin.register(SignupModel)
class SignupModelAdmin(admin.ModelAdmin):
    list_display =['id','username','email','password']


