from django.contrib import admin
from .models import Item, Image, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ModuleInline(admin.StackedInline):
    model = Image


@admin.register(Item)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ModuleInline]
