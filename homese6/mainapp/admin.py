from django.contrib import admin
from .models import Jewel, Category

# Register your models here.
class JewelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Jewel, JewelAdmin)
admin.site.register(Category, CategoryAdmin)