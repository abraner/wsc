# Generated by Django 3.2 on 2022-03-14 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0120_contractincludetotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractincludetotal',
            name='bid_idA',
        ),
        migrations.RemoveField(
            model_name='contractincludetotal',
            name='ident',
        ),
        migrations.RemoveField(
            model_name='contractincludetotal',
            name='includeid',
        ),
        migrations.RemoveField(
            model_name='contractincludetotal',
            name='pageid',
        ),
    ]