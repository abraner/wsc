# Generated by Django 3.2 on 2022-01-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0023_alter_bidtbl_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerinfo',
            old_name='idA',
            new_name='custid',
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='prodqueue',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='prodqueue',
            name='production',
            field=models.CharField(blank=True, max_length=50, unique=True, verbose_name='Production'),
        ),
    ]
