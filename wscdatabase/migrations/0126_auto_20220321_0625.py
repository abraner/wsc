# Generated by Django 3.2 on 2022-03-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0125_contract_customdeposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='forthdeposit',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
        migrations.AddField(
            model_name='contract',
            name='seconddeposit',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
        migrations.AddField(
            model_name='contract',
            name='thirddeposit',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
    ]
