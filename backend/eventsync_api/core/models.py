from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

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
    cpf = models.CharField(max_length=11, unique=True,
                           validators=[cpf_validator])
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
        ordering = ['id']


EVENT_STATUS_CHOICES = [
    ('upcoming', _('Upcoming')),
    ('ongoing', _('Ongoing')),
    ('completed', _('Completed')),
    ('cancelled', _('Cancelled')),
]

EVENT_TYPE_CHOICES = [
    ('conference', _('Conference')),
    ('workshop', _('Workshop')),
    ('seminar', _('Seminar')),
    ('meetup', _('Meetup')),
]


class Event(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    hours_quantity = models.IntegerField()
    description = models.TextField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=EVENT_STATUS_CHOICES, default='upcoming')
    event_type = models.CharField(
        max_length=20, choices=EVENT_TYPE_CHOICES, default='conference')

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['id']
        

class ThemeRoom(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.TimeField()
    
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    hours_quantity = models.IntegerField()
    description = models.TextField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES, default='upcoming')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='conference')

    class Meta:
        verbose_name = "Theme Room"
        verbose_name_plural = "Theme Rooms"
        ordering = ['id']

    def clean(self):
        # Call the parent class's clean method to ensure any inherited validation is executed
        super().clean()
        
        # Ensure start_date and end_date are within the Event's date range
        if self.start_date < self.event.start_date or self.end_date > self.event.end_date:
            raise ValidationError('The start date and end date of the Theme Room must be within the Event\'s date range.')

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    phone = models.CharField(max_length=11, validators=[phone_validator])
    email = models.EmailField(_("email address"), unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
        ordering = ['id']

    def __str__(self):
        return self.nome


class Sponsorship(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
        ordering = ['id']

    def __str__(self):
        return f"{self.sponsor.name} - {self.event.name}"

