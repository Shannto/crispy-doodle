from stock.models import Product
from django.contrib import admin
from .models import  History, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(History)
