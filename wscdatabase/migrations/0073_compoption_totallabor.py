# Generated by Django 3.2 on 2022-02-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0072_alter_compoption_totalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='compoption',
            name='totallabor',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name=''),
        ),
    ]
