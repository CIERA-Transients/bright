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
    grb_name = models.CharField(max_length=1000, help_text='Name of GRB')

    comments = RichTextField(help_text='Additional info about the GRB that may be of note')

    ra_host = models.CharField(max_length=100,
        null=True, blank=True, verbose_name='Right Ascension of Host', help_text='Right Ascension, in degrees.'
    )
    dec_host = models.CharField(max_length=100,
        null=True, blank=True, verbose_name='Declination of Host', help_text='Declination, in degrees.'
    )
    tel_pos = models.CharField(max_length=100,
        null=True, blank=True, verbose_name='Telescope Position', help_text='Telescope from which sky location is derived'
    )
    tel_pos_ref = models.CharField(max_length=100,
        null=True, blank=True, verbose_name='Telescope Reference', help_text='Reference for sky location information.'
    )

    host_morphology = models.CharField(max_length=100,
        null=True, blank=True, verbose_name='Host Galaxy Morphology', help_text='Host galaxy Morphology.'
    )

    host_sf = models.CharField(max_length=100,
        null=True, blank=True, verbose_name='Host Galaxy Star Formation', help_text='Host Galaxy Star Formation.'
    )

    pcc = models.FloatField(
            null=True, blank=True, verbose_name='Probability of belonging to host galaxy', help_text='Probability of belonging to host galaxy'
    )

    t90 = models.FloatField(
            null=True, blank=True, verbose_name='T 90', help_text='??'
    )

    t90_err_upper = models.FloatField(
            null=True, blank=True, verbose_name='T 90', help_text='??'
    )

    t90_err_lower = models.FloatField(
            null=True, blank=True, verbose_name='T 90', help_text='??'
    )

    fluence = models.FloatField(
            null=True, blank=True, verbose_name='Fluence', help_text='??'
    )
    fluence_err_upper = models.FloatField(
            null=True, blank=True, verbose_name='Fluence Upper Error', help_text='??'
    )
    fluence_err_lower = models.FloatField(
            null=True, blank=True, verbose_name='Fluence Lower Error', help_text='??'
    )

    xray = models.CharField(max_length=3,
        null=True, blank=True, verbose_name='Reference', help_text='Reference for sky location information.'
    )
    opt = models.CharField(max_length=3,
        null=True, blank=True, verbose_name='Reference', help_text='Reference for sky location information.'
    )
    radio = models.CharField(max_length=3,
        null=True, blank=True, verbose_name='Reference', help_text='Reference for sky location information.'
    )


    offset = models.FloatField(
        null=True, blank=True, verbose_name='Offset', help_text='Offset'
    )
    offset_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Offset Upper Error', help_text='Offset Upper Error'
    )
    offset_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Offset Lower Error', help_text='Offset Lower Error'
    )

    offset_kpc = models.FloatField(
        null=True, blank=True, verbose_name='Offset KPC', help_text='Offset in KPC'
    )
    offset_kpc_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Offset KPC Upper Error', help_text='Offset KPC Upper Error'
    )
    offset_kpc_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Offset KPC Lower Error', help_text='Offset KPC Lower Error'
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
    z_ref = models.CharField(max_length=100,null=True, blank=True,)

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
        null=True, blank=True, verbose_name='Gas Log Solar Metallicity', help_text='Gas Log Solar Metallicity.'
    )
    gas_logz_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Gas Log Solar Metallicity Upper Error', help_text='Gas Log Solar Metallicity Upper Error'
    )
    gas_logz_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Gas Log Solar Metallicity Lower Error', help_text='Gas Log Solar Metallicity Lower Error'
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

    sfr = models.FloatField(
        null=True, blank=True, verbose_name='Star Formation Rate', help_text='Star Formation Rate.'
    )
    sfr_err_upper = models.FloatField(
        null=True, blank=True, verbose_name='Star Formation Rate Upper Error', help_text='Star Formation Rate Upper Error'
    )
    sfr_err_lower = models.FloatField(
        null=True, blank=True, verbose_name='Star Formation Rate Lower Error', help_text='Star Formation Rate Lower Error'
    )

    phot = ArrayField(models.FloatField(null=True, blank=True,), blank=True, null=True)
    phot_err = ArrayField(models.FloatField(null=True, blank=True,), blank=True, null=True)
    phot_wave = ArrayField(models.FloatField(null=True, blank=True,), blank=True, null=True)
    phot_refs = ArrayField(models.CharField(max_length=100,null=True, blank=True,), blank=True, null=True)
    filters = ArrayField(models.CharField(max_length=100,null=True, blank=True,), blank=True, null=True)
    telescopes = ArrayField(models.CharField(max_length=100,null=True, blank=True,), blank=True, null=True)


    spec = models.FileField(upload_to='observed_spectrum/', null=True, blank=True, validators=[validate_file_extension])
    spec_tel = models.CharField(max_length=100,null=True, blank=True,)
    spec_ref = models.CharField(max_length=100,null=True, blank=True,)

    mod_phot = models.FileField(upload_to='model_phot/', null=True, blank=True, validators=[validate_file_extension])
    mod_spec = models.FileField(upload_to='model_spectrum/', null=True, blank=True, validators=[validate_file_extension])
    
    corner = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image_extension])

    sed = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image_extension])

    color = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image_extension])

    h5 = models.FileField(upload_to='samples/', null=True, blank=True, validators=[validate_file_extension])

    json_metadata = models.FileField(upload_to='json/', null=True, blank=True, validators=[validate_file_extension])

    gcn = models.URLField(max_length=300,
        null=True, blank=True, verbose_name='URL for GCN', help_text='URL for GCN'
    )

    def __str__(self):
        return self.grb_name


class Fits(models.Model):
    grb = models.ForeignKey(GRB, on_delete=models.CASCADE)
    fits = models.FileField(upload_to='fits/', null=True, blank=True, validators=[validate_file_extension])
    def __str__(self):
        return "Fits File {0} which is associated with {1}".format(self.fits, self.grb.grb_name)

class Reference(models.Model):
    grb = models.ForeignKey(GRB, on_delete=models.CASCADE)
    shorthand = models.CharField(max_length=100,
        null=True, blank=True, verbose_name='Citation short hand', help_text='Citation short hand'
    )
    url = models.URLField(max_length=300,
        null=True, blank=True, verbose_name='URL for reference', help_text='URL for reference'
    )
    def __str__(self):
        return "Citation {0} which is associated with {1}".format(self.shorthand, self.grb.grb_name)
