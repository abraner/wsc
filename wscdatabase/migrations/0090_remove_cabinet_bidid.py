# Generated by Django 3.2 on 2022-03-04 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0089_rename_ident_cabinet_jobid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabinet',
            name='bidid',
        ),
    ]
