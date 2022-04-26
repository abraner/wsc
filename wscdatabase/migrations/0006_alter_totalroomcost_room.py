# Generated by Django 3.2 on 2021-12-13 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0005_alter_totalroomcost_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalroomcost',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='wscdatabase.roomtype', to_field='room_type', verbose_name='Room'),
        ),
    ]
