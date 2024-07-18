from django.shortcuts import render
from catalog.models import Product

def base(request):
    prod = Product.objects.all()
    context = {"products": prod}
    return render(request, 'catalog/product.html', context)

def product_detail(request, pk):
    prod = Product.objects.get(pk=pk)
    context = {"products": prod}
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')

