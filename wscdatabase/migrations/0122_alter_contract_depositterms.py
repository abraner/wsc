# Generated by Django 3.2 on 2022-03-16 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0121_auto_20220313_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='depositterms',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='term', to='wscdatabase.terms', verbose_name=''),
        ),
    ]
