# Generated by Django 3.2 on 2022-03-11 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0104_auto_20220311_0758'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Excluded',
        ),
        migrations.DeleteModel(
            name='Included',
        ),
    ]
