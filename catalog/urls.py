from django.urls import path
from catalog.views import base, contacts, product_detail

urlpatterns = [
    path('', base),
    path('product/<int:pk>/', product_detail),
    path('contacts/', contacts),
]