# Generated by Django 3.2 on 2022-04-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0154_auto_20220410_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cabacc',
            options={'verbose_name': 'Accssorie'},
        ),
        migrations.AlterModelTable(
            name='cabacc',
            table='CabAcc',
        ),
    ]
