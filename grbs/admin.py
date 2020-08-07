from django.contrib import admin

# Register your models here.
from .models import GRB, Fits

admin.site.register(GRB)
admin.site.register(Fits)
