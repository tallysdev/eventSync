# Generated by Django 5.0.4 on 2024-08-18 17:36

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be 11 digits.', regex='^\\d{11}$')])),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FormsRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('Discursiva', 'Discursiva'), ('Múltipla escolha', 'Múltipla escolha'), ('Objetiva', 'Objetiva')], default='Discursiva', max_length=20)),
                ('options', models.JSONField(blank=True, default=list)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formsregister')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sponsor')),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ThemeRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('speaker', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('hours_quantity', models.IntegerField()),
                ('audiences', models.TextField()),
                ('max_quantity', models.IntegerField()),
                ('min_quantity', models.IntegerField()),
                ('local', models.TextField()),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='upcoming', max_length=20)),
                ('event_type', models.CharField(choices=[('conference', 'Conference'), ('workshop', 'Workshop'), ('seminar', 'Seminar'), ('meetup', 'Meetup')], default='conference', max_length=20)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
            ],
            options={
                'verbose_name': 'Theme Room',
                'verbose_name_plural': 'Theme Rooms',
                'ordering': ['id'],
            },
        ),
    ]
