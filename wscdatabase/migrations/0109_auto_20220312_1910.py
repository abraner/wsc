# Generated by Django 3.2 on 2022-03-13 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0108_auto_20220312_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='includedoption',
            old_name='descriptionnum',
            new_name='comp',
        ),
        migrations.RenameField(
            model_name='includedoption',
            old_name='name',
            new_name='compname',
        ),
        migrations.RenameField(
            model_name='includedoption',
            old_name='qty',
            new_name='compqty',
        ),
    ]
