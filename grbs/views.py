from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import GRB, Fits, Reference
from .forms import GRBForm, DownloadForm
from django.contrib.auth.decorators import user_passes_test
import zipfile
import io
# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    alphabetical_grbs_list = GRB.objects.filter(type_grb="short").order_by('grb_name')
    context = {'alphabetical_grbs_list': alphabetical_grbs_list}
    return render(request, 'grbs/index.html', context)

@user_passes_test(lambda u: u.is_superuser)
def lgrb(request):
    alphabetical_grbs_list = GRB.objects.filter(type_grb="long").order_by('grb_name')
    context = {'alphabetical_grbs_list': alphabetical_grbs_list}
    return render(request, 'grbs/lgrb_index.html', context)

@user_passes_test(lambda u: u.is_superuser)
def detail(request, grb_id):
    grb = get_object_or_404(GRB, pk=grb_id)
    fits_files = Fits.objects.filter(grb=grb_id) 
    references = Reference.objects.filter(grb=grb_id)
    references_dict = {}
    for ref in references:
        references_dict[ref.shorthand] = ref.url

    if not fits_files:
        phot_zip = zip(grb.phot, grb.phot_err, grb.telescopes, grb.phot_refs, grb.filters, len(grb.filters)*[None])
    else:
        phot_zip = zip(grb.phot, grb.phot_err, grb.telescopes, grb.phot_refs, grb.filters, fits_files)

    if grb.type_grb == "short":
        return render(request, 'grbs/short_detail.html', {'grb': grb, 'phot_zip' : phot_zip, 'references': references_dict})
    else:
        return render(request, 'grbs/long_detail.html', {'grb': grb, 'phot_zip' : phot_zip, 'references': references_dict})

def download(request, grb_ids):
    grb = get_object_or_404(GRB, pk=grb_id)
    return render(request, 'grbs/detail.html', {'grb': grb})

def function(request):
    if request.method == 'POST':
        form = GRBForm(request.POST)
        if form.is_valid():
            new_grb = form.save(commit=False)
            new_grb.save()
            return redirect(function_that_happens_at_url)

def function_that_happens_at_url(request):
    if request.user.is_superuser:
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


def bulkdownload_all(request):
    if request.method == 'GET':
        form = DownloadForm(request.GET)
        if form.is_valid():
            grbs_ids_to_download = list(filter(None,form.cleaned_data['grbs'].split(',')))
            response = HttpResponse(content_type='application/zip')
            with zipfile.ZipFile(response, 'w') as zf:
                for grb_id in grbs_ids_to_download:
                    grb = get_object_or_404(GRB, pk=grb_id)
                    try:
                        zf.write(grb.corner.file.name, arcname=grb.corner.name)
                    except:
                        pass
                    try:
                        zf.write(grb.color.file.name, arcname=grb.color.name)
                    except:
                        pass
                    try:
                        zf.write(grb.sed.file.name, arcname=grb.sed.name)
                    except:
                        pass
                    try:
                        zf.write(grb.h5.file.name, arcname=grb.h5.name)
                    except:
                        pass
                    try:
                        zf.write(grb.mod_phot.file.name, arcname=grb.mod_phot.name)
                    except:
                        pass
                    try:
                        zf.write(grb.mod_spec.file.name, arcname=grb.mod_spec.name)
                    except:
                        pass
                    try:
                        zf.write(grb.json_metadata.file.name, arcname=grb.json_metadata.name)
                    except:
                        pass
            ZIPFILE_NAME = 'grb_alldata.zip'
            response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
            return response
        return redirect("grbs:index")
    else:
        return redirect("grbs:index")

def bulkdownload_json(request):
    if request.method == 'GET':
        form = DownloadForm(request.GET)
        if form.is_valid():
            grbs_ids_to_download = list(filter(None,form.cleaned_data['grbs'].split(',')))
            response = HttpResponse(content_type='application/zip')
            with zipfile.ZipFile(response, 'w') as zf:
                for grb_id in grbs_ids_to_download:
                    grb = get_object_or_404(GRB, pk=grb_id)
                    try:
                        zf.write(grb.json_metadata.file.name, arcname=grb.json_metadata.name)
                    except:
                        pass
            ZIPFILE_NAME = 'grb_json_metadata.zip'
            response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
            return response
        return redirect("grbs:index")
    else:
        return redirect("grbs:index")

def bulkdownload_samples(request):
    if request.method == 'GET':
        form = DownloadForm(request.GET)
        if form.is_valid():
            grbs_ids_to_download = list(filter(None,form.cleaned_data['grbs'].split(',')))
            response = HttpResponse(content_type='application/zip')
            with zipfile.ZipFile(response, 'w') as zf:
                for grb_id in grbs_ids_to_download:
                    grb = get_object_or_404(GRB, pk=grb_id)
                    try:
                        zf.write(grb.h5.file.name, arcname=grb.h5.name)
                    except:
                        pass
            ZIPFILE_NAME = 'grb_samples.zip'
            response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
            return response
        return redirect("grbs:index")
    else:
        return redirect("grbs:index")

def bulkdownload_plots(request):
    if request.method == 'GET':
        form = DownloadForm(request.GET)
        if form.is_valid():
            grbs_ids_to_download = list(filter(None,form.cleaned_data['grbs'].split(',')))
            response = HttpResponse(content_type='application/zip')
            with zipfile.ZipFile(response, 'w') as zf:
                for grb_id in grbs_ids_to_download:
                    grb = get_object_or_404(GRB, pk=grb_id)
                    try:
                        zf.write(grb.corner.file.name, arcname=grb.corner.name)
                    except:
                        pass
                    try:
                        zf.write(grb.color.file.name, arcname=grb.color.name)
                    except:
                        pass
                    try:
                        zf.write(grb.sed.file.name, arcname=grb.sed.name)
                    except:
                        pass
            ZIPFILE_NAME = 'grb_plots.zip'
            response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
            return response
        return redirect("grbs:index")
    else:
        return redirect("grbs:index")

def bulkdownload_fits_and_models(request):
    if request.method == 'GET':
        form = DownloadForm(request.GET)
        if form.is_valid():
            grbs_ids_to_download = list(filter(None,form.cleaned_data['grbs'].split(',')))
            response = HttpResponse(content_type='application/zip')
            with zipfile.ZipFile(response, 'w') as zf:
                for grb_id in grbs_ids_to_download:
                    grb = get_object_or_404(GRB, pk=grb_id)
                    zf.write(grb.mod_phot.file.name, arcname=grb.mod_phot.name)
                    zf.write(grb.mod_spec.file.name, arcname=grb.mod_spec.name)
            ZIPFILE_NAME = 'grb_fits_and_models.zip'
            response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
            return response
        return redirect("grbs:index")
    else:
        return redirect("grbs:index")
