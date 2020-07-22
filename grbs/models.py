from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class GRB(models.Model):
    """Model that defines metadata about a grb

        :param grb_name: Name of grb being sold.
        :type grb_name: str

        :param description: Description of grb being sold.
        :type description: str
    """
    grb_name = models.CharField(max_length=200, help_text='Name of GRB')
    description = RichTextField(help_text='Additional info about the GRB that may be of note')
    ra = models.FloatField(
        null=True, blank=True, verbose_name='Right Ascension', help_text='Right Ascension, in degrees.'
    )
    dec = models.FloatField(
        null=True, blank=True, verbose_name='Declination', help_text='Declination, in degrees.'
    )
    def __str__(self):
        return self.grb_name
