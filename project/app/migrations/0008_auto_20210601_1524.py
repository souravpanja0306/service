# Generated by Django 3.1.5 on 2021-06-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210601_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentonemi',
            name='refNo',
            field=models.IntegerField(),
        ),
    ]
