# Generated by Django 5.0.3 on 2024-04-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_rename_organizationizer_event_organizer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='event_date_and_time',
        ),
    ]
