# Generated by Django 3.2 on 2022-01-03 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0026_alter_customerinfo_prodqueue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='prodqueue',
            field=models.ForeignKey(blank=True, default='A', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prodqueue', to='wscdatabase.prodqueue', to_field='production', verbose_name=''),
        ),
    ]
