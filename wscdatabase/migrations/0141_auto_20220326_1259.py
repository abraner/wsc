# Generated by Django 3.2 on 2022-03-26 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0140_alter_totalroomcost_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalroomcost',
            name='rmname',
            field=models.CharField(default=1, max_length=45, verbose_name='Address #1:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comp24', to='wscdatabase.roomtype', verbose_name='Room'),
        ),
    ]