# Generated by Django 3.2 on 2022-03-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0117_contractinclude_bidid'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractinclude',
            name='pageid',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]
