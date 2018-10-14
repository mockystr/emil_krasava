from django.urls import path, re_path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.AvailableItemsListView.as_view(), name="index"),
    path('categories', views.CategoryListView.as_view(), name='category_list'),
    path('about_us', views.AboutUsView.as_view(), name='about_us'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('<slug:category_slug>', views.CategoryProductsListView.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
