from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# Create your views here.

def index(request):
    alphabetical_products_list = Product.objects.order_by('product_name')
    context = {'alphabetical_products_list': alphabetical_products_list}
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail2.html', {'product': product})

def function(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.save()
            return redirect(function_that_happens_at_url)

def function_that_happens_at_url(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.save()
                return redirect('/')
        else:
            form = ProductForm()
        return render(request, 'products/add_product.html', {'form' : form})
    else:
        return redirect('/accounts/login')
