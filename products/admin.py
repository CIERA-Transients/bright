from django.contrib import admin

# Register your models here.
from .models import Product, Pricing, Media

admin.site.register(Pricing)
admin.site.register(Media)

class MediaStacked(admin.StackedInline):
    model = Media

class PricingStacked(admin.StackedInline):
    model = Pricing

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PricingStacked, MediaStacked]
