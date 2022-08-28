from django.contrib.auth.models import User, AbstractUser
from django.db import models
# from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

from django.db import models
from django.core.mail import send_mail
# from django.contrib.auth.models import PermissionsMixin, User, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                     "allowed.")

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_company = models.BooleanField(default=False)
  is_talent = models.BooleanField(default=False)


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.ethnicity


class Role(models.Model):
    GENDER_REQUIREMENTS = (
        ("Female", "Female"),
        ("Male", "Male"),
        ("Non-binary", "Non-binary"),
        ("Prefer Not To Say", "Prefer Not To Say")
    )
    role_name = models.CharField(max_length=255, null=False, default="Role Name")
    talent_age = models.IntegerField()
    talent_gender = models.CharField(choices=GENDER_REQUIREMENTS, default="Prefer Not To Say", max_length=250)
    talent_ethnicity = models.ForeignKey(Ethnicity, models.SET_NULL, null=True, related_name=' role set+')
    talent_weight = models.DecimalField(max_digits=6, max_length=10, decimal_places=2)
    talent_height = models.DecimalField(max_digits=6, max_length=10, decimal_places=2)

    def __str__(self):
        return self.talent_gender


class Application(models.Model):
    applicant_name = models.CharField(max_length=255)
    # name = models.ForeignKey(Talent, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default="Role")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_name

class Talent(models.Model):
    GENDER_CHOICES = (
        ("Female", "Female"),
        ("Male", "Male"),
        ("Non-binary", "Non-binary"),
        ("Prefer Not To Say", "Prefer Not To Say")
    )
    talent_name = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='talent', default="")
    # name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    # listmusic_choice = models.TextField(max_length=300)
    gender = models.CharField(choices=GENDER_CHOICES, default="Prefer Not To Say", max_length=250)
    # gender_custom = models.CharField(max_length=200, blank=True)
    ethnicity = models.ForeignKey(Ethnicity, models.SET_NULL, null=True, related_name='talent ethnicity+')
    age = models.CharField(max_length=3)
    weight = models.DecimalField(max_digits=6, max_length=10, decimal_places=4, null=True)
    height = models.DecimalField(max_digits=6, max_length=10, decimal_places=4, null=True)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.talent_name


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Talent.objects.create(name=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.talent.save()


class Company(models.Model):  #company_profile
    company_name = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, default="")
    # company_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=255)
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE, null=False)
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.project_name


class random_table(models.Model):
    pass
