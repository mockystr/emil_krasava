from django.contrib import admin
from .models import Item, Image, Category, Catalog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ImageInline(admin.StackedInline):
    model = Image


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageInline]


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
