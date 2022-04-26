# Generated by Django 3.2 on 2022-03-17 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0123_auto_20220317_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='depositperc',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='depositperc', to='wscdatabase.percentage', to_field='multiplier', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='percentage',
            name='multiplier',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=7, unique=True, verbose_name=''),
        ),
    ]