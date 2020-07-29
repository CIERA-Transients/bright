from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from .validators import validate_file_extension, validate_image_extension
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class GRB(models.Model):
    """Model that defines metadata about a grb

        :param grb_name: Name of grb being sold.
        :type grb_name: str

        :param description: Description of grb being sold.
        :type description: str
    """
    grb_name = models.CharField(max_length=200, help_text='Name of GRB')

    comments = RichTextField(help_text='Additional info about the GRB that may be of note')

    ra = models.FloatField(
        null=True, blank=True, verbose_name='Right Ascension', help_text='Right Ascension, in degrees.'
    )

    dec = models.FloatField(
        null=True, blank=True, verbose_name='Declination', help_text='Declination, in degrees.'
    )

    z = models.FloatField(
        null=True, blank=True, verbose_name='Red Shift', help_text='Red Shift'
    )

    t_90 = models.FloatField(
            null=True, blank=True, verbose_name='Red Shift', help_text='??'
    )

    mass = models.FloatField(
        null=True, blank=True, verbose_name='Mass', help_text='Mass'
    )

    age = models.FloatField(
        null=True, blank=True, verbose_name='Age', help_text='Age'
    )

    logzsol = models.FloatField(
        null=True, blank=True, verbose_name='Log Solar Metallicity', help_text='Log Solar Metallicity.'
    )

    gas_logz = models.FloatField(
        null=True, blank=True, verbose_name='Log Gas Metallicity', help_text='Log Gas Metallicity.'
    )

    dust1 = models.FloatField(
        null=True, blank=True, verbose_name='dust1', help_text='dust1.'
    )

    dust2 = models.FloatField(
        null=True, blank=True, verbose_name='dust2', help_text='dust2.'
    )

    gas_logu = models.FloatField(
        null=True, blank=True, verbose_name='Log Gas ??', help_text='Log Gas ??.'
    )

    sfr = models.FloatField(
        null=True, blank=True, verbose_name='SFR', help_text='SFR, in degrees.'
    )

    phot = ArrayField(models.FloatField())

    phot_error = ArrayField(models.FloatField())

    filters = ArrayField(models.CharField(max_length=100))

    spectrogram = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image_extension])

    samples = models.FileField(upload_to='samples/', null=True, default=None, validators=[validate_file_extension])
    def __str__(self):
        return self.grb_name
