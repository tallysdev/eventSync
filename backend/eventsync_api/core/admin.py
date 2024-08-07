from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import ESUser, Local, Event, Sponsor, Sponsorship
from .forms import CustomUserCreationForm, CustomUserChangeForm


class ESUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = ESUser
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
         'fields': ('name', 'cpf', 'birth_date', 'phone')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'cpf', 'birth_date', 'phone', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(ESUser, ESUserAdmin)


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('local_name', 'street_name',
                    'street_number', 'city', 'state', 'cep')
    search_fields = ('local_name', 'city', 'state', 'cep')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date',
                    'local', 'status', 'event_type')
    list_filter = ('status', 'event_type', 'local')
    search_fields = ('name', 'description')
    date_hierarchy = 'start_date'


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')


@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ('event', 'sponsor')
    list_filter = ('event', 'sponsor')
    search_fields = ('event_name', 'sponsor_name')
