# Generated by Django 3.2 on 2022-03-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0105_auto_20220311_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='workorderdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
