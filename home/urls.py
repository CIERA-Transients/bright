from django.urls import path
from django.views.generic import TemplateView


app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name='home'),
    path('sgrbs', TemplateView.as_view(template_name='home/sgrbs.html'), name='sgrbs'),
    path('pop-properties', TemplateView.as_view(template_name='home/pop_properties.html'), name='pop_properties'),
    path('data-products-description', TemplateView.as_view(template_name='home/downloadable_data.html'), name='downloadable_data'),
]
