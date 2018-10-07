from django.shortcuts import render
from .models import Category, Item, Image
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# class AvailableItemsMixin(object):
#     def get_queryset(self):
#         qs = super(AvailableItemsMixin, self).get_queryset()
#         return qs.filter(available=True)


class AvailableItemsListView(TemplateResponseMixin, View):
    model = Category
    template_name = 'main/index.html'

    def get(self, request):
        categories = Category.objects.all()
        return self.render_to_response({'categories': categories})


class CategoryProductsListView(TemplateResponseMixin, View):
    template_name = 'main/list.html'

    def get(self, request, category_slug):
        # module = get_object_or_404(Category, slug=category_slug)
        category = get_object_or_404(Category, slug=category_slug)
        items_of_category = Item.objects.filter(category=category)
        return self.render_to_response({'items': items_of_category})


class ProductDetailView(TemplateResponseMixin, View):
    template_name = 'main/detail.html'

    def get(self, request, id, slug):
        item = get_object_or_404(Item, id=id, slug=slug)
        return self.render_to_response({'item': item})
