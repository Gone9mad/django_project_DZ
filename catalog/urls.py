from django.urls import path
from catalog.views import (ProductListView, ContactsTemplateView, ProductDetailView, BlogCreateView, BlogUpdateView,
                           BlogDetailView, BlogDeleteView, BlogListView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsTemplateView.as_view()),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('blog/', BlogListView.as_view(), name='blog'),
]