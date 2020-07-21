from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Product(models.Model):
    """Model that defines metadata about a product

        :param product_name: Name of product being sold.
        :type product_name: str

        :param description: Description of product being sold.
        :type description: str
    """
    product_name = models.CharField(max_length=200)
    description = RichTextField()
    def __str__(self):
        return self.product_name

class Pricing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    cost_per_item = models.FloatField()
    charge_tax = models.BooleanField()

class Media(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    media = models.ImageField(upload_to='images/')
