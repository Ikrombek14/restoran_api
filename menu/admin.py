from django.contrib import admin
from .models import MenuCategory, MenuProducts, MenuOrder
# Register your models here.


admin.site.register(MenuCategory)
admin.site.register(MenuProducts)
admin.site.register(MenuOrder)
