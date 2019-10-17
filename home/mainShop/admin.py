from django.contrib import admin
#Product - The class created in mainShop/models.py
from . models import Product, Contact, Orders

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)