# Generated by Django 3.2.3 on 2021-05-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210529_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='custimerId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
