# Generated by Django 3.2 on 2022-02-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0078_auto_20220228_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcost',
            name='custom_currency',
        ),
        migrations.AlterField(
            model_name='jobcost',
            name='custom',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
    ]
