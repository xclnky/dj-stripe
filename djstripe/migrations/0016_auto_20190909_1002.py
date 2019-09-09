# Generated by Django 2.2.4 on 2019-09-09 10:02

from django.db import migrations
import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0015_customer_default_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancetransaction',
            name='type',
            field=djstripe.fields.StripeEnumField(enum=djstripe.enums.BalanceTransactionType, max_length=29),
        ),
    ]
