# Generated by Django 3.2 on 2022-03-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0138_contractinclude_rmactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractincludetotal',
            name='includeid',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]
