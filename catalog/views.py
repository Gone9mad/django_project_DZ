from django.shortcuts import render
from catalog.models import Product, BlogPost
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.utils.text import slugify



class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

class BlogListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'date_of_creation', 'publication')
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'date_of_creation', 'publication')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail', args=[self.kwargs.get('pk')])


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blog')
