# Generated by Django 3.1.5 on 2021-07-12 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20210612_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='status',
            field=models.CharField(choices=[('Pendig', 'pendig'), ('Processing', 'Processing'), ('Done', 'Done')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='service',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partsname',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='partsname',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paymentonemi',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='techname',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
