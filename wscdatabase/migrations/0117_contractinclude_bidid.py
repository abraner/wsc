# Generated by Django 3.2 on 2022-03-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0116_contractinclude_ident'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractinclude',
            name='bidid',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]