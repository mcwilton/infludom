from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                     "allowed.")


# class User(AbstractUser):
#   is_company = models.BooleanField(default=False)
#   email = models.EmailField(max_length=255)


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=200)

    def __str__(self):
        return self.ethnicity


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
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default="Role")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_name


class Company(models.Model): 
    company_name = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, default="")
    # company_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.company_name

# @receiver(post_save, sender=User)
# def create_company_profile(sender, instance, created, **kwargs):
#     if created:
#         Company.objects.create(company_name=instance)


# @receiver(post_save, sender=User)
# def save_company_profile(sender, instance, **kwargs):
#     instance.company.save()


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=255)
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE, null=False)
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.project_name