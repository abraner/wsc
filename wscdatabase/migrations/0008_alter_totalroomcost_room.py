# Generated by Django 3.2 on 2021-12-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0007_alter_totalroomcost_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalroomcost',
            name='room',
            field=models.IntegerField(default=None, null=True, verbose_name='Room'),
        ),
    ]