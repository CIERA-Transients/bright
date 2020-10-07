from django.urls import path

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
]
