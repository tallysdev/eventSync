from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import ESUserManager

cpf_validator = RegexValidator(
    regex=r'^\d{11}$',
    message=_("CPF must be 11 digits.")
)

phone_validator = RegexValidator(
    regex=r'^\d{11}$',
    message=_("Phone number must be 11 digits.")
)

class ESUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, validators=[phone_validator])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['cpf', 'name', 'birth_date', 'phone', 'user_type']

    objects = ESUserManager()

    def __str__(self):
        return self.email

class Local(models.Model):
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    reference = models.CharField(max_length=255, blank=True, null=True)
    local_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.local_name} - {self.street_name}, {self.street_number}, {self.city}, {self.state}, {self.cep}"

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locals"

# class Event(models.Model):
#     name = models.CharField(max_length=150)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     max_quantity = models.IntegerField()
#     min_quantity = models.IntegerField()
#     hours_quantity = models.IntegerField()




