from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from grbs.models import GRB, Fits, Reference

import glob
import json
import os

class Command(BaseCommand):
    help = 'Command to update or make new GRB for the bright.ciera.northwestern.edu webserver'

    def add_arguments(self, parser):
        parser.add_argument("--json-file", required=True)
        parser.add_argument("--path-to-data", required=True)

    def handle(self, *args, **options):
        if not os.path.isfile(options['json_file']):
            raise ValueError("Provided JSON file does not exist")

        if not os.path.isdir(options['path_to_data']):
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
            # construct path to data directory
            data_dir = os.path.join(options['path_to_data'], grb_name.upper())
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
                        grb.corner.save(v[0], File(open(os.path.join(data_dir, v[0]), 'rb')))
                    except:
                        grb.corner.save(v, File(open(os.path.join(data_dir, v), 'rb')))
                elif k.lower() == 'sed':
                    try:
                        grb.sed.save(v[0], File(open(os.path.join(data_dir, v[0]), 'rb')))
                    except:
                        grb.sed.save(v, File(open(os.path.join(data_dir, v), 'rb')))
                elif k.lower() == 'color':
                    try:
                        grb.color.save(v[0], File(open(os.path.join(data_dir, v[0]), 'rb')))
                    except:
                        grb.color.save(v, File(open(os.path.join(data_dir, v), 'rb')))
                elif k.lower() == 'h5':
                    try:
                        grb.h5.save(v[0], File(open(os.path.join(data_dir, v[0]), 'rb')))
                    except:
                        grb.h5.save(v, File(open(os.path.join(data_dir, v), 'rb')))
                elif k.lower() == 'mod_phot':
                    try:
                        grb.mod_phot.save(v[0], File(open(os.path.join(data_dir, v[0]), 'rb')))
                    except:
                        grb.mod_phot.save(v, File(open(os.path.join(data_dir, v), 'rb')))
                elif k.lower() == 'mod_spec':
                    try:
                        grb.mod_spec.save(v[0], File(open(os.path.join(data_dir, v[0]), 'rb')))
                    except:
                        grb.mod_spec.save(v, File(open(os.path.join(data_dir, v), 'rb')))
                elif k.lower() == 'urls':
                    for reference, url in v.items():
                        ref = Reference(grb=grb, shorthand=reference, url=url)
                        ref.save()
                else:
                    setattr(grb, k.lower(), v)
            grb.save()

            # finally we save the fits files
            for fits_file in glob.glob(os.path.join(data_dir, "*.fits")):
                fits = Fits(grb=grb)
                fits_file_name = os.path.basename(fits_file)
                fits.fits.save(fits_file_name, File(open(fits_file, 'rb')))
                fits.save()
