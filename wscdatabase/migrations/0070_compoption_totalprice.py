# Generated by Django 3.2 on 2022-02-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0069_labor_bid_ida'),
    ]

    operations = [
        migrations.AddField(
            model_name='compoption',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
    ]
