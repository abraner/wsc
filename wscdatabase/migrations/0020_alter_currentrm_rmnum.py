# Generated by Django 3.2 on 2021-12-23 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0019_auto_20211223_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentrm',
            name='rmnum',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rmnum', to='wscdatabase.roomtype', verbose_name='Room'),
        ),
    ]