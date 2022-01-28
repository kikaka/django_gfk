# Generated by Django 4.0.1 on 2022-01-25 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['name'], 'permissions': (('can_say_hello', 'Set event active'),)},
        ),
    ]
