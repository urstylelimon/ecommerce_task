from django.contrib import admin

from .models import User, Category, Product


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','full_name', 'email', 'is_staff', 'is_superuser')

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price', 'description', 'category')