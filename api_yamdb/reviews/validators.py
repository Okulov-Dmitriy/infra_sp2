from django.core.exceptions import ValidationError
import datetime as dt


def validate_year(self, value):
    if value > dt.date.today().year:
        raise ValidationError(
            'Год выпуска не может быть больше текущего.'
        )
    return value
