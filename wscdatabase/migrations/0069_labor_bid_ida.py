# Generated by Django 3.2 on 2022-02-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0068_rename_bid_ida_labor_jobid'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor',
            name='bid_idA',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]
