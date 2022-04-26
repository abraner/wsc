# Generated by Django 3.2 on 2021-12-22 16:46

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0017_rename_total_qty_compoptiontotal_compqty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabacccustom',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Custom Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabaccrmcost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Custom Acc. Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabaccrmtotal',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Cabinet Accessories'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabacctotal',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Custom Cabinet Acc.Total'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabinet',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Cabinet Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabsidecost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Side Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabsidetotal',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Price for Sides'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='cabtotalprice',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Price for Cabinets'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='custcabcost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Custom Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='custcabtotal',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Custom Cabinet Total'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='custsidecost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Custom Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='custsidetotal',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Custom Sides Total'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='drawercost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Drawer Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='drawertotal',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Price for Drawers'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='optioncost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Option Cost'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='optionnum',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Cabinet Options'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='optiontotal',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Price for Options'),
        ),
        migrations.AlterField(
            model_name='totalroomcost',
            name='totalrmcost',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0.00'), default_currency='USD', max_digits=14, null=True, verbose_name='Total Room Cost'),
        ),
    ]
