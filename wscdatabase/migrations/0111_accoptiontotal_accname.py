# Generated by Django 3.2 on 2022-03-13 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0110_includedacc'),
    ]

    operations = [
        migrations.AddField(
            model_name='accoptiontotal',
            name='accname',
            field=models.CharField(blank=True, max_length=50, verbose_name=''),
        ),
    ]
