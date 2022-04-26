# Generated by Django 3.2 on 2022-02-22 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0054_alter_jobcost_discounttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcost',
            name='customtext',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext', to='wscdatabase.contractoption', verbose_name='Custom Text'),
        ),
        migrations.AlterField(
            model_name='jobcost',
            name='discounttext',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discounttext', to='wscdatabase.contractoption', verbose_name='Discount Text'),
        ),
    ]
