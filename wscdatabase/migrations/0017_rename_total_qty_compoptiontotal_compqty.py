# Generated by Django 3.2 on 2021-12-20 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0016_accoptiontotal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compoptiontotal',
            old_name='total_qty',
            new_name='compqty',
        ),
    ]
