from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import Product


# Create your views here.
class HomePageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'all_products'


class ContactPageView(TemplateView):

    template_name = 'contact.html'


class AboutPageView(TemplateView):

    template_name = 'about.html'


class AllProductsPageView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'all_products'


class SingleProductPageView(DetailView):
    model = Product
    template_name = 'single_product.html'
    context_object_name = 'product'

