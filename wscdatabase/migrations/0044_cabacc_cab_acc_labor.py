# Generated by Django 3.2 on 2022-01-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0043_auto_20220124_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabacc',
            name='cab_acc_labor',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]