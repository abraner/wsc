# Generated by Django 3.2 on 2022-01-10 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0036_auto_20220108_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='totalroomcost',
            name='cabaccrmcost',
        ),
        migrations.RemoveField(
            model_name='totalroomcost',
            name='cabaccrmcost_currency',
        ),
        migrations.RemoveField(
            model_name='totalroomcost',
            name='optioncost',
        ),
        migrations.RemoveField(
            model_name='totalroomcost',
            name='optioncost_currency',
        ),
        migrations.RemoveField(
            model_name='totalroomcost',
            name='optiontotal',
        ),
        migrations.RemoveField(
            model_name='totalroomcost',
            name='optiontotal_currency',
        ),
    ]