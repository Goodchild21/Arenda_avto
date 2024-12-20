from django.contrib import admin
from cars.models import Categories, Products
# admin.site.register(Categories)
# admin.site.register(Products)

#Регистрация моделей
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}