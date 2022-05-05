from django.urls import path
from .views import HomePageView, ContactPageView, AboutPageView, AllProductsPageView, SingleProductPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', AllProductsPageView.as_view(), name='products'),
    path('single_product/<slug>/', SingleProductPageView.as_view(), name='single_product')
]
