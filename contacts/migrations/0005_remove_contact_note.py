# Generated by Django 3.2.4 on 2021-06-17 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_contact_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='note',
        ),
    ]
