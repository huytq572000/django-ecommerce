from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price',]
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class CategoryAdmin(admin.ModelAdmin):
    ...
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category,CategoryAdmin)