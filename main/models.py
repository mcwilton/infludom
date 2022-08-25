from django.db import models

from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                     "allowed.")


# Create your models here.

class Creator(models.Model):
    STATUS_CHOICES = (
        ("Female", "Female"),
        ("Male", "Male"),
        ("Non-binary", "Non-binary"),
        ("Prefer Not To Say", "Prefer Not To Say")
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    music_choice = models.TextField(max_length=300)
    status = models.CharField(choices=STATUS_CHOICES, default="Prefer Not To Say", max_length=250)
