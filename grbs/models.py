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

    ra = models.CharField(max_length=20,
        null=True, blank=True, verbose_name='Right Ascension', help_text='Right Ascension, in degrees.'
    )

    dec = models.CharField(max_length=20,
        null=True, blank=True, verbose_name='Declination', help_text='Declination, in degrees.'
    )

    z = models.FloatField(
        null=True, blank=True, verbose_name='Red Shift', help_text='Red Shift'
    )
    z_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Red Shift Upper Error', help_text='Red Shift Upper Error'
    )
    z_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Red Shift Lower Error', help_text='Red Shift Lower Error'
    )

    t_90 = models.FloatField(
            null=True, blank=True, verbose_name='T 90', help_text='??'
    )

    mass = models.FloatField(
        null=True, blank=True, verbose_name='Mass', help_text='Mass'
    )
    mass_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Mass Upper Error', help_text='Mass Upper Error'
    )
    mass_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Mass Lower Error', help_text='Mass Lower Error'
    )

    age = models.FloatField(
        null=True, blank=True, verbose_name='Age', help_text='Age'
    )
    age_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Age Upper Error', help_text='Age Upper Error'
    )
    age_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Age Lower Error', help_text='Age Lower Error'
    )

    logzsol = models.FloatField(
        null=True, blank=True, verbose_name='Log Solar Metallicity', help_text='Log Solar Metallicity.'
    )
    logzsol_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Log Solar Metallicity Upper Error', help_text='Log Solar Metallicity Upper Error'
    )
    logzsol_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Log Solar Metallicity Lower Error', help_text='Log Solar Metallicity Lower Error'
    )

    gas_logz = models.FloatField(
        null=True, blank=True, verbose_name='Log Gas Metallicity', help_text='Log Gas Metallicity.'
    )

    dust1 = models.FloatField(
        null=True, blank=True, verbose_name='dust1', help_text='dust1.'
    )
    dust1_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Dust1 Upper Error', help_text='Dust1 Upper Error'
    )
    dust1_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Dust1 Lower Error', help_text='Dust1 Lower Error'
    )

    dust2 = models.FloatField(
        null=True, blank=True, verbose_name='dust2', help_text='dust2.'
    )
    dust2_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Dust2 Upper Error', help_text='Dust2 Upper Error'
    )
    dust2_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Dust2 Lower Error', help_text='Dust2 Lower Error'
    )

    gas_logu = models.FloatField(
        null=True, blank=True, verbose_name='Log Gas ??', help_text='Log Gas ??.'
    )

    sfr = models.FloatField(
        null=True, blank=True, verbose_name='Star Formation Rate', help_text='Star Formation Rate.'
    )
    sfr_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Star Formation Rate Upper Error', help_text='Star Formation Rate Upper Error'
    )
    sfr_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Star Formation Rate Lower Error', help_text='Star Formation Rate Lower Error'
    )

    phot = ArrayField(models.FloatField())
    phot_err_upper = ArrayField(models.FloatField())
    phot_err_lower = ArrayField(models.FloatField())

    filters = ArrayField(models.CharField(max_length=100))

    spectrogram = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image_extension])

    samples = models.FileField(upload_to='samples/', null=True, default=None, validators=[validate_file_extension])
    def __str__(self):
        return self.grb_name
