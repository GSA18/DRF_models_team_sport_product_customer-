from django.contrib import admin
from .models import Team, Sport, Product, Customer


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class SportAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','price']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'num_doc','phone']   


admin.site.register(Team, TeamAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)