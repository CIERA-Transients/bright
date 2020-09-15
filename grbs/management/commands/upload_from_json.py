from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from grbs.models import GRB, Fits

import glob
import json
import os

class Command(BaseCommand):
    help = 'Command to update or make new GRB for the bright.ciera.northwestern.edu webserver'

    def add_arguments(self, parser):
        parser.add_argument("--json-file", required=True)

    def handle(self, *args, **options):
        if not os.path.isfile(options['json_file']):
            raise ValueError("Provided JSON file does not exist")

        # Change into the directory where the JSON file is, this should contain
        # also all the files assocaited with this GRB
        os.chdir(os.path.dirname(options['json_file']))

        # Get the full path to the json file
        json_file = os.path.basename(options['json_file'])

        with open(json_file, 'r') as f:
            grb_metadata = json.load(f)
            # get grb_name from json file
            grb_name = json_file.replace('.json', '')
            # see if GRB already exists
            grb = GRB.objects.filter(grb_name=grb_name).first()
            # does not exist need to create a new GRB
            if grb is None:
                grb = GRB(grb_name=grb_name)

            grb.json_metadata.save(json_file, File(open(json_file, 'rb')))

            for k, v in grb_metadata.items():
                # set attributes of model from JSON key, value pairs
                if k.lower() == 'corner':
                    try:
                        grb.corner.save(v[0], File(open(v[0], 'rb')))
                    except:
                        grb.corner.save(v, File(open(v, 'rb')))
                elif k.lower() == 'sed':
                    try:
                        grb.sed.save(v[0], File(open(v[0], 'rb')))
                    except:
                        grb.sed.save(v, File(open(v, 'rb')))
                elif k.lower() == 'color':
                    try:
                        grb.color.save(v[0], File(open(v[0], 'rb')))
                    except:
                        grb.color.save(v, File(open(v, 'rb')))
                elif k.lower() == 'h5':
                    try:
                        grb.h5.save(v[0], File(open(v[0], 'rb')))
                    except:
                        grb.h5.save(v, File(open(v, 'rb')))
                elif k.lower() == 'mod_phot':
                    try:
                        grb.mod_phot.save(v[0], File(open(v[0], 'rb')))
                    except:
                        grb.mod_phot.save(v, File(open(v, 'rb')))
                elif k.lower() == 'mod_spec':
                    try:
                        grb.mod_spec.save(v[0], File(open(v[0], 'rb')))
                    except:
                        grb.mod_spec.save(v, File(open(v, 'rb')))
                else:
                    setattr(grb, k.lower(), v)
            grb.save()

            # finally we save the fits files
            for fits_file in glob.glob("*.fits"):
                fits = Fits(grb=grb)
                fits.fits.save(fits_file, File(open(fits_file, 'rb')))
                fits.save()
