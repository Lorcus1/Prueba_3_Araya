# Generated by Django 3.2.3 on 2021-06-16 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210615_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='magen',
            new_name='Imagen',
        ),
    ]
