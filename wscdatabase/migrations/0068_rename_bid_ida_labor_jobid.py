# Generated by Django 3.2 on 2022-02-25 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0067_alter_labor_labor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labor',
            old_name='bid_idA',
            new_name='jobid',
        ),
    ]