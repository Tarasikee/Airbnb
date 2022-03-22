from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    GENDER_CHOICES = ((GENDER_MALE, "Male"), (GENDER_FEMALE, "Female"), (GENDER_OTHER, "Other"),)

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_UKRANIAN = 'ua'
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, 'English'), (LANGUAGE_UKRANIAN, 'Ukranian'),)

    CURRENCY_USD = 'usd'
    CURRENCY_UAH = 'uah'
    CURRENCY_CHOICES = ((CURRENCY_USD, 'USD'), (CURRENCY_UAH, 'UAH'),)

    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    bio = models.TextField(default='', blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
