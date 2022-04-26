# Generated by Django 3.2 on 2022-03-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0128_auto_20220321_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcost',
            name='constructionamount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
        migrations.AddField(
            model_name='jobcost',
            name='customamount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
        migrations.AddField(
            model_name='jobcost',
            name='discountamount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
        migrations.AddField(
            model_name='jobcost',
            name='opt2amount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
        migrations.AddField(
            model_name='jobcost',
            name='opt3amount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
    ]