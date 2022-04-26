# Generated by Django 3.2 on 2022-01-07 20:56

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0034_auto_20220107_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totals',
            name='totalincrease',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=7, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='totals',
            name='totalrmcost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=7, null=True, verbose_name='Total Room Cost'),
        ),
    ]
