# Generated by Django 3.2 on 2022-02-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0049_jobcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcost',
            name='custadd1',
            field=models.CharField(blank=True, default=None, max_length=45, null=True, verbose_name='Address #1:'),
        ),
        migrations.AddField(
            model_name='jobcost',
            name='custlastname',
            field=models.CharField(blank=True, default=None, max_length=45, null=True, verbose_name='Last Name:'),
        ),
    ]
