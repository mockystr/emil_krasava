from django.shortcuts import render
from .models import Category, Item, Image
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class AvailableItemsListView(TemplateResponseMixin, View):
    model = Category
    template_name = 'main/index.html'

    def get(self, request):
        categories = Category.objects.all()
        return self.render_to_response({'categories': categories})


class CategoryProductsListView(TemplateResponseMixin, View):
    template_name = 'main/item_list.html'

    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        items_of_category = Item.objects.filter(category=category)
        return self.render_to_response({'items': items_of_category})


class ProductDetailView(TemplateResponseMixin, View):
    template_name = 'main/detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["other_images"] = Image.objects.filter(item=id)
    #     return context

    def get(self, request, id, slug):
        item = get_object_or_404(Item, id=id, slug=slug)
        return self.render_to_response({'item': item,
                                        'other_images': Image.objects.filter(item=id)})


class CategoryListView(TemplateResponseMixin, View):
    template_name = 'main/categories_list.html'

    def get(self, request):
        categories = Category.objects.all()
        return self.render_to_response({'categories': categories})


class AboutUsView(TemplateResponseMixin, View):
    template_name = 'main/company_info/about_us.html'

    def get(self, request):
        return self.render_to_response({})


class ContactsView(TemplateResponseMixin, View):
    template_name = 'main/company_info/contacts.html'

    def get(self, request):
        return self.render_to_response({})
