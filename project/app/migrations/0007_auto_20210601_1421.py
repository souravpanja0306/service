# Generated by Django 3.1.5 on 2021-06-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_paymentonemi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentonemi',
            old_name='PaidAmount',
            new_name='paidAmount',
        ),
        migrations.RenameField(
            model_name='paymentonemi',
            old_name='PaymentDate',
            new_name='paymentDate',
        ),
    ]
