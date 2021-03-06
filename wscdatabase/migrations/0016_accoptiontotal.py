# Generated by Django 3.2 on 2021-12-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0015_auto_20211219_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccOptionTotal',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('bidid', models.IntegerField(default=None, null=True, verbose_name='')),
                ('bid_idA', models.IntegerField(default=None, null=True, verbose_name='')),
                ('custid', models.IntegerField(default=None, null=True, verbose_name='')),
                ('conid', models.IntegerField(default=None, null=True, verbose_name='')),
                ('saleid', models.IntegerField(default=None, null=True, verbose_name='')),
                ('total_qty', models.IntegerField(default=None, null=True, verbose_name='')),
                ('acc', models.IntegerField(default=None, null=True, verbose_name='')),
                ('price', models.DecimalField(decimal_places=2, default='0.00', max_digits=7, verbose_name='')),
            ],
        ),
    ]
