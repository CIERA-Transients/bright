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
    z = models.FloatField(
        null=True, blank=True, verbose_name='Red Shift', help_text='Red Shift, in degrees.'
    )
    mass = models.FloatField(
        null=True, blank=True, verbose_name='Mass', help_text='Mass, in degrees.'
    )
    age = models.FloatField(
        null=True, blank=True, verbose_name='Age', help_text='Age, in degrees.'
    )
    Z_stellar = models.FloatField(
        null=True, blank=True, verbose_name='Metallicity', help_text='Metallicity, in degrees.'
    )
    Z_gas = models.FloatField(
        null=True, blank=True, verbose_name='Gas Metallicity', help_text='Gas Metallicity, in degrees.'
    )
    tau = models.FloatField(
        null=True, blank=True, verbose_name='TAU', help_text='TAU, in degrees.'
    )
    AV = models.FloatField(
        null=True, blank=True, verbose_name='AV', help_text='AV, in degrees.'
    )
    SFR = models.FloatField(
        null=True, blank=True, verbose_name='SFR', help_text='SFR, in degrees.'
    )
    spectrogram = models.ImageField(upload_to='images/', null=True, blank=True, )
    def __str__(self):
        return self.grb_name
