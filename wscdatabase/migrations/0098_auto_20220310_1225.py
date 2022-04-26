# Generated by Django 3.2 on 2022-03-10 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wscdatabase', '0097_auto_20220310_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='Construction',
            new_name='construction',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='ConstructionText',
            new_name='constructiontext',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Custom',
            new_name='custom',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='CustomText',
            new_name='customtext',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Deposit',
            new_name='deposit',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='DepositDate',
            new_name='depositdate',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='DepositPerc',
            new_name='depositperc',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='DepositTerms',
            new_name='depositterms',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Discount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='DiscountText',
            new_name='discounttext',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='FinalPayment',
            new_name='finalpayment',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='FinalPaymentDate',
            new_name='finalpaymentdate',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='FinalPerc',
            new_name='finalperc',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='GrandTotalCost',
            new_name='grandtotalcost',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Install',
            new_name='install',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo1',
            new_name='memo1',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo10',
            new_name='memo10',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo11',
            new_name='memo11',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo12',
            new_name='memo12',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo13',
            new_name='memo13',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo14',
            new_name='memo14',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo15',
            new_name='memo15',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo16',
            new_name='memo16',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo17',
            new_name='memo17',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo2',
            new_name='memo2',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo3',
            new_name='memo3',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo4',
            new_name='memo4',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo5',
            new_name='memo5',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo6',
            new_name='memo6',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo7',
            new_name='memo7',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo8',
            new_name='memo8',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Memo9',
            new_name='memo9',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='OPt3Num',
            new_name='opt3num',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Opt3Text',
            new_name='opt3text',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Pay2Perc',
            new_name='pay2perc',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Pay3Perc',
            new_name='pay3perc',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Pay4Perc',
            new_name='pay4perc',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Payment2',
            new_name='payment2',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Payment2Date',
            new_name='payment2date',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Payment3',
            new_name='payment3',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Payment3Date',
            new_name='payment3date',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Payment4',
            new_name='payment4',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Payment4Date',
            new_name='payment4date',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='SubTotalCost',
            new_name='subtotalcost',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Tax',
            new_name='tax',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='TaxRate',
            new_name='taxrate',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Terms2',
            new_name='terms2',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Terms3',
            new_name='terms3',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='Terms4',
            new_name='terms4',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='TermsFinal',
            new_name='termsfinal',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='TotalJobCost',
            new_name='totaljobcost',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='TotalRmCost',
            new_name='totalrmcost',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='WorkType',
            new_name='worktype',
        ),
    ]
