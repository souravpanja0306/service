# Generated by Django 3.2.3 on 2021-06-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_customerdetails_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='advanceAmount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='dueAmount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='totalAmount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paymentonemi',
            name='paidAmount',
            field=models.IntegerField(),
        ),
    ]