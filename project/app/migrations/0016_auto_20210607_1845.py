# Generated by Django 3.1.5 on 2021-06-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_partsname_servicemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentonemi',
            name='cashCheque',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paymentonemi',
            name='chequeNo',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
