from django.contrib import admin

# Register your models here.
from .models import GRB, Fits, Reference

admin.site.register(GRB)
admin.site.register(Fits)
admin.site.register(Reference)
