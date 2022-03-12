from django.core.exceptions import ValidationError


def has_letters_only_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')

    return value


def validate_file_size(value):
    max_size_in_mb = 5
    filesize = value.size

    if filesize > max_size_in_mb * 1024 * 1024:
        raise ValidationError(f"The maximum file size that can be uploaded is {max_size_in_mb}MB")
    else:
        return value

