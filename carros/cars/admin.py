from django.contrib import admin
from .models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')
    list_filter = ('factory_year', 'model_year')
    ordering = ('id',)



class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('id',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)