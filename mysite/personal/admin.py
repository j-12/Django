from django.contrib import admin
from .models import Product, Cart, user_info

admin.site.register(Product)
admin.site.register(Cart)
# Register your models here.
admin.site.register(user_info)
