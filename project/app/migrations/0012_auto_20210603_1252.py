# Generated by Django 3.1.5 on 2021-06-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210601_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetails',
            name='emi',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='modelNameTwo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='modelNoTwo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='quantityTwo',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
