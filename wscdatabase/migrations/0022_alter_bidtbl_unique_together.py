# Generated by Django 3.2 on 2021-12-28 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0021_alter_bidtbl_c11qty'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bidtbl',
            unique_together={('custid', 'room')},
        ),
    ]
