# Generated by Django 3.2 on 2022-03-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0085_auto_20220303_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabinet',
            name='roomid',
            field=models.IntegerField(default=None, null=True, verbose_name=''),
        ),
    ]
