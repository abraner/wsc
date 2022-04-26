# Generated by Django 3.2 on 2022-02-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0056_jobcost_taxrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcost',
            name='taxrate',
            field=models.DecimalField(decimal_places=4, default='0.0000', max_digits=7, verbose_name='Tax Rate'),
        ),
    ]
