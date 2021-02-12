from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'grbs'
urlpatterns = [
    # ex: /grbs/
    path('', views.index, name='index'),
    # ex: /grbs/1/
    path('<int:grb_id>/', views.detail, name='detail'),
    # ex: /grbs/add_grb
    path('add_grb', views.function_that_happens_at_url, name='add_grb'),
    # ex: /grbs/add_grb_from_form
    path('add_grb_from_form/', views.function, name='add_grb_from_form'),
    path('bulkdownload-all/', views.bulkdownload_all, name='bulkdownload_all'),
    path('bulkdownload-json/', views.bulkdownload_json, name='bulkdownload_json'),
    path('bulkdownload-samples/', views.bulkdownload_samples, name='bulkdownload_samples'),
    path('bulkdownload-plots/', views.bulkdownload_plots, name='bulkdownload_plots'),
    path('sgrbs', TemplateView.as_view(template_name='home/sgrbs.html'), name='sgrbs'),
    path('pop-properties', TemplateView.as_view(template_name='home/pop_properties.html'), name='pop_properties'),
    path('data-products-description', TemplateView.as_view(template_name='home/downloadable_data.html'), name='downloadable_data'),

    # lgrb catalogue
    path('lgrb-catalogue/', views.lgrb, name='lgrb'),
]
