from django.contrib import admin
from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)

from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
