from django.contrib import admin
#Product - The class created in mainShop/models.py
from . models import Product

admin.site.register(Product)