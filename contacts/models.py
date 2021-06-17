from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# from django.db.models.fields import DateField
from localflavor.us.models import USStateField, USZipCodeField


class Contact(models.Model):
    note = models.ForeignKey(
        'Note',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Note(models.Model):
    note = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
