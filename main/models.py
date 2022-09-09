from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                     "allowed.")

class User(AbstractUser):

  is_talent = models.BooleanField(default=False)


class Talent_Ethnicity(models.Model):
    
    ethnicity = models.CharField(max_length=200)

    def __str__(self):
        return self.ethnicity


class Talent(models.Model):

    GENDER_CHOICES = (
        ("Female", "Female"),
        ("Male", "Male"),
        ("Non-binary", "Non-binary"),
        ("Prefer Not To Say", "Prefer Not To Say")
    )
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='talent', default="")
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, default="Prefer Not To Say", max_length=25)
    ethnicity = models.ForeignKey(Talent_Ethnicity, models.SET_NULL, null=True, related_name='talent ethnicity+')
    age = models.CharField(max_length=3)
    weight = models.DecimalField(max_digits=6, max_length=10, decimal_places=4, null=True)
    height = models.DecimalField(max_digits=6, max_length=10, decimal_places=4, null=True)
    # weight = models.FloatField()
    # height = models.FloatField()
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.talent.username

if User.is_talent == True:
    @receiver(post_save, sender=User)
    def create_talent_profile(sender, instance, created, **kwargs):
        if created:
            Talent.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_talent_profile(sender, instance, **kwargs):
        instance.talent.save()

else:
    pass



