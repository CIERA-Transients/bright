from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    # ex: /products/
    path('', views.index, name='index'),
    # ex: /products/1/
    path('<int:product_id>/', views.detail, name='detail'),
    # ex: /products/add_product
    path('add_product', views.function_that_happens_at_url, name='add_product'),
    # ex: /products/add_product_from_form
    path('add_product_from_form/', views.function, name='add_product_from_form')
]
