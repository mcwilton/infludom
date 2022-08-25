from django.db import models

from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                     "allowed.")


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.ethnicity


class Talent(models.Model):
    GENDER_CHOICES = (
        ("Female", "Female"),
        ("Male", "Male"),
        ("Non-binary", "Non-binary"),
        ("Prefer Not To Say", "Prefer Not To Say")
    )
    ETHNICITY_CHOICES = (
        ("", "Female"),
        ("Male", "Male"),
        ("Non-binary", "Non-binary"),
        ("Prefer Not To Say", "Prefer Not To Say")
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    music_choice = models.TextField(max_length=300)
    status = models.CharField(choices=GENDER_CHOICES, default="Prefer Not To Say", max_length=250)
    gender_custom = models.CharField(max_length=200, blank=True)
    ethnicity = models.ForeignKey(Ethnicity, models.SET_NULL, null=True)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=6, max_length=10, decimal_places=4)
    height = models.DecimalField(max_digits=6, max_length=10, decimal_places=4)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
