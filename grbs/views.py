from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import GRB
from .forms import GRBForm
# Create your views here.

def index(request):
    alphabetical_grbs_list = GRB.objects.order_by('grb_name')
    context = {'alphabetical_grbs_list': alphabetical_grbs_list}
    return render(request, 'grbs/index.html', context)

def detail(request, grb_id):
    grb = get_object_or_404(GRB, pk=grb_id)
    return render(request, 'grbs/detail2.html', {'grb': grb})

def function(request):
    if request.method == 'POST':
        form = GRBForm(request.POST)
        if form.is_valid():
            new_grb = form.save(commit=False)
            new_grb.save()
            return redirect(function_that_happens_at_url)

def function_that_happens_at_url(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GRBForm(request.POST)
            if form.is_valid():
                new_grb = form.save(commit=False)
                new_grb.save()
                return redirect('/')
        else:
            form = GRBForm()
        return render(request, 'grbs/add_grb.html', {'form' : form})
    else:
        return redirect('/accounts/login')
