# Generated by Django 3.2 on 2022-04-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0143_alter_bidtbl_comp32'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractinclude',
            name='bidid',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='contractincludetotal',
            name='bidid',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]
