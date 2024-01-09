from django.contrib import admin

# Register your models here.
from api.models import Category,Product,Basket,BasketItem


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketItem)