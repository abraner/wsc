# Generated by Django 3.2 on 2022-03-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0134_auto_20220325_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalroomcost',
            name='rmactive',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]
