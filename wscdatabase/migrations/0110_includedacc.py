# Generated by Django 3.2 on 2022-03-13 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0109_auto_20220312_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncludedAcc',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='')),
                ('custid', models.IntegerField(default=None, null=True, verbose_name='')),
                ('accqty', models.IntegerField(default=None, null=True, verbose_name='')),
                ('acc', models.IntegerField(default=None, null=True, verbose_name='')),
                ('accname', models.CharField(blank=True, max_length=150, verbose_name='')),
            ],
        ),
    ]
