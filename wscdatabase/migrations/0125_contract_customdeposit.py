# Generated by Django 3.2 on 2022-03-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0124_auto_20220317_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='customdeposit',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
    ]
