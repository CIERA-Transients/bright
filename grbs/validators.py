def validate_image_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.png', '.jpg',]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported image extension.')

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.h5', '.hdf5', '.fits']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
