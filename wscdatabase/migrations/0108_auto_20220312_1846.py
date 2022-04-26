# Generated by Django 3.2 on 2022-03-12 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0107_includedoption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='includedoption',
            old_name='description',
            new_name='descriptionnum',
        ),
        migrations.AddField(
            model_name='includedoption',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name=''),
        ),
    ]
